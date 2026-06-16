
import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(
    page_title='CRM Food Delivery Dashboard',
    layout='wide'
)

FINAL_DATA_PATH = "data/processed/food_delivery_crm_final_result.csv"
OUTPUT_DIR = "outputs"

df = pd.read_csv(FINAL_DATA_PATH)
model_result = pd.read_csv(OUTPUT_DIR + '/model_comparison_result.csv')
feature_importance = pd.read_csv(OUTPUT_DIR + '/feature_importance_result.csv')
crm_strategy = pd.read_csv(OUTPUT_DIR + '/crm_strategy_matrix.csv')
customer_priority = pd.read_csv(OUTPUT_DIR + '/customer_priority_table.csv')

st.title('CRM Dashboard Food Delivery')
st.write('Prediksi risiko churn, segmentasi risiko, feature importance, dan strategi CRM.')

def pct(value):
    return f'{value:.1f}%'

def get_top_value(data, column):
    if column not in data.columns or len(data) == 0:
        return '-'
    value_counts = data[column].dropna().value_counts()
    if len(value_counts) == 0:
        return '-'
    return value_counts.index[0]

def get_top_count(data, column):
    if column not in data.columns or len(data) == 0:
        return 0
    value_counts = data[column].dropna().value_counts()
    if len(value_counts) == 0:
        return 0
    return int(value_counts.iloc[0])

def make_output_insight(data):
    if len(data) == 0:
        return 'Tidak ada data pada filter ini. Ubah filter untuk melihat insight.'
    
    total = len(data)
    risk_count = int((data['Output'] == 'No').sum())
    safe_count = int((data['Output'] == 'Yes').sum())
    risk_rate = risk_count / total * 100
    
    return (
        f'Dari {total} pelanggan terfilter, {risk_count} pelanggan atau {risk_rate:.1f}% masuk kategori risiko churn. '
        f'Artinya, fokus CRM perlu diarahkan ke pelanggan Output No karena kelompok ini berpotensi tidak membeli ulang. '
        f'Sementara {safe_count} pelanggan masih menunjukkan kecenderungan beli ulang.'
    )

def make_segment_insight(data):
    if len(data) == 0:
        return 'Tidak ada data pada filter ini. Ubah filter untuk melihat insight.'
    
    top_segment = get_top_value(data, 'risk_segment')
    top_count = get_top_count(data, 'risk_segment')
    total = len(data)
    top_percent = top_count / total * 100
    
    if top_segment == 'High Risk':
        action = 'Prioritas utama adalah campaign retensi cepat, seperti voucher fast delivery, kompensasi delay, dan pesan personal.'
    elif top_segment == 'Medium Risk':
        action = 'Kelompok ini masih berpeluang dipertahankan melalui loyalty point, promo personal, dan rekomendasi restoran.'
    elif top_segment == 'Low Risk':
        action = 'Kelompok ini cocok untuk program referral, membership, dan reward review positif.'
    else:
        action = 'Gunakan segmen risiko untuk menentukan prioritas campaign.'
    
    return (
        f'Segmen terbesar pada data terfilter adalah {top_segment} dengan {top_count} pelanggan atau {top_percent:.1f}%. '
        f'So what: {action}'
    )

def make_model_insight(model_df):
    if len(model_df) == 0:
        return 'Belum ada hasil evaluasi model.'
    
    best_model = model_df.sort_values('f1_score', ascending=False).iloc[0]
    
    return (
        f'Model dengan F1-score tertinggi adalah {best_model["model"]} dengan F1-score {best_model["f1_score"]:.3f}. '
        f'F1-score penting karena data memiliki kelas risiko yang lebih kecil. '
        f'Artinya, model tidak hanya dinilai dari akurasi, tetapi juga dari kemampuan menangkap pelanggan berisiko.'
    )

def make_feature_insight(feature_df):
    if len(feature_df) == 0:
        return 'Belum ada feature importance.'
    
    top_feature = feature_df.iloc[0]['feature_clean']
    top_importance = feature_df.iloc[0]['importance']
    
    return (
        f'Faktor paling penting menurut model adalah {top_feature} dengan nilai importance {top_importance:.3f}. '
        f'So what: faktor ini perlu menjadi dasar penyusunan strategi CRM karena paling membantu model membedakan pelanggan berisiko dan tidak berisiko.'
    )

def make_priority_insight(data):
    if len(data) == 0:
        return 'Tidak ada pelanggan pada filter ini.'
    
    top_customer = data.sort_values('risk_score', ascending=False).iloc[0]
    name = top_customer.get('customer_name', 'Pelanggan prioritas')
    score = top_customer['risk_score']
    segment = top_customer['risk_segment']
    reason = top_customer['reason_code']
    action = top_customer['crm_action']
    
    return (
        f'Pelanggan prioritas tertinggi adalah {name} dengan risk score {score:.3f}, segmen {segment}, dan alasan utama {reason}. '
        f'So what: tindakan CRM yang disarankan adalah {action}.'
    )

def make_map_insight(data):
    if len(data) == 0:
        return 'Tidak ada titik lokasi pada filter ini.'
    
    return (
        f'Peta menampilkan sebaran {len(data)} pelanggan sesuai filter. '
        f'So what: area dengan pelanggan berisiko tinggi dapat dipakai untuk prioritas campaign lokal, rekomendasi restoran terdekat, dan optimasi layanan delivery.'
    )

def make_strategy_insight(data):
    return (
        'CRM Strategy Matrix menghubungkan risk segment, karakteristik pelanggan, strategi, channel, dan KPI. '
        'So what: strategi tidak dibagikan sama rata ke semua pelanggan, tetapi disesuaikan dengan risiko dan alasan churn.'
    )

total_customer = len(df)
actual_risk_rate = df['churn_risk'].mean() * 100
high_risk = (df['risk_segment'] == 'High Risk').sum()
medium_risk = (df['risk_segment'] == 'Medium Risk').sum()
low_risk = (df['risk_segment'] == 'Low Risk').sum()

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric('Total Customer', total_customer)
col2.metric('Actual Risk Rate', pct(actual_risk_rate))
col3.metric('High Risk', high_risk)
col4.metric('Medium Risk', medium_risk)
col5.metric('Low Risk', low_risk)

st.info(
    f'Dashboard ini memetakan {total_customer} pelanggan. '
    f'Actual risk rate sebesar {actual_risk_rate:.1f}% menunjukkan proporsi pelanggan yang berisiko tidak membeli ulang. '
    f'So what: pelanggan High Risk dan Medium Risk perlu menjadi prioritas retensi.'
)

st.divider()

st.sidebar.header('Filter Dashboard')

risk_options = ['All'] + sorted(df['risk_segment'].dropna().unique().tolist())
segment_filter = st.sidebar.selectbox('Risk Segment', risk_options)

reason_options = ['All'] + sorted(df['reason_code'].dropna().unique().tolist())
reason_filter = st.sidebar.selectbox('Reason Code', reason_options)

if 'Gender' in df.columns:
    gender_options = ['All'] + sorted(df['Gender'].dropna().unique().tolist())
    gender_filter = st.sidebar.selectbox('Gender', gender_options)
else:
    gender_filter = 'All'

if 'Occupation' in df.columns:
    occupation_options = ['All'] + sorted(df['Occupation'].dropna().unique().tolist())
    occupation_filter = st.sidebar.selectbox('Occupation', occupation_options)
else:
    occupation_filter = 'All'

min_score = st.sidebar.slider(
    'Minimal Risk Score',
    min_value=0.0,
    max_value=1.0,
    value=0.0,
    step=0.05
)

top_n = st.sidebar.slider(
    'Jumlah Pelanggan Ditampilkan',
    min_value=5,
    max_value=100,
    value=20,
    step=5
)

filtered_df = df.copy()

if segment_filter != 'All':
    filtered_df = filtered_df[filtered_df['risk_segment'] == segment_filter]

if reason_filter != 'All':
    filtered_df = filtered_df[filtered_df['reason_code'] == reason_filter]

if gender_filter != 'All':
    filtered_df = filtered_df[filtered_df['Gender'] == gender_filter]

if occupation_filter != 'All':
    filtered_df = filtered_df[filtered_df['Occupation'] == occupation_filter]

filtered_df = filtered_df[filtered_df['risk_score'] >= min_score]

st.subheader('Analisis Data Terfilter')
if len(filtered_df) > 0:
    col_a, col_b = st.columns(2)
    with col_a:
        reason_count = filtered_df['reason_code'].value_counts().reset_index()
        reason_count.columns = ['Reason Code', 'Jumlah']
        fig_reason = px.bar(reason_count, x='Reason Code', y='Jumlah', color='Reason Code', text='Jumlah', title='Distribusi Alasan Risiko')
        fig_reason.update_traces(textposition='outside')
        fig_reason.update_layout(xaxis_title='Reason Code', yaxis_title='Jumlah Pelanggan', showlegend=False)
        st.plotly_chart(fig_reason, use_container_width=True)
    with col_b:
        fig_score = px.histogram(filtered_df, x='risk_score', nbins=10, title='Distribusi Risk Score')
        fig_score.update_layout(xaxis_title='Risk Score', yaxis_title='Frekuensi')
        st.plotly_chart(fig_score, use_container_width=True)
else:
    st.warning('Tidak ada pelanggan pada kombinasi filter ini.')

left, right = st.columns(2)

with left:
    st.subheader('Distribusi Output')
    output_count = filtered_df['Output'].value_counts().reset_index()
    output_count.columns = ['Output', 'Jumlah']
    fig_output = px.bar(output_count, x='Output', y='Jumlah', color='Output', text='Jumlah')
    fig_output.update_traces(textposition='outside')
    fig_output.update_layout(xaxis_title='Output', yaxis_title='Jumlah Pelanggan', showlegend=False)
    st.plotly_chart(fig_output, use_container_width=True)

    st.info(make_output_insight(filtered_df))

with right:
    st.subheader('Distribusi Risk Segment')
    segment_count = filtered_df['risk_segment'].value_counts().reset_index()
    segment_count.columns = ['Risk Segment', 'Jumlah']
    fig_segment = px.bar(segment_count, x='Risk Segment', y='Jumlah', color='Risk Segment', text='Jumlah')
    fig_segment.update_traces(textposition='outside')
    fig_segment.update_layout(xaxis_title='Risk Segment', yaxis_title='Jumlah Pelanggan', showlegend=False)
    st.plotly_chart(fig_segment, use_container_width=True)

    st.info(make_segment_insight(filtered_df))

st.subheader('Model Comparison')
st.dataframe(model_result, use_container_width=True, hide_index=True)
st.info(make_model_insight(model_result))

st.subheader('Top Feature Importance')
if len(feature_importance) > 0:
    top_features = feature_importance.head(15).sort_values('importance', ascending=True)
    fig_feat = px.bar(top_features, x='importance', y='feature_clean', orientation='h', text='importance')
    fig_feat.update_traces(texttemplate='%{text:.3f}', textposition='outside')
    fig_feat.update_layout(xaxis_title='Importance', yaxis_title='Feature')
    st.plotly_chart(fig_feat, use_container_width=True)

st.info(make_feature_insight(feature_importance))

st.subheader('Customer Priority Table')

priority_cols = [
    'customer_id',
    'customer_name',
    'risk_score',
    'risk_segment',
    'reason_code',
    'crm_action',
    'crm_channel',
    'crm_kpi',
    'Age',
    'Gender',
    'Marital Status',
    'Occupation',
    'Monthly Income'
]

available_cols = [col for col in priority_cols if col in filtered_df.columns]

priority_view = (
    filtered_df[available_cols]
    .sort_values('risk_score', ascending=False)
    .head(top_n)
    .reset_index(drop=True)
)

st.dataframe(
    priority_view,
    use_container_width=True,
    hide_index=True
)

st.info(make_priority_insight(priority_view))

csv_download = priority_view.to_csv(index=False).encode('utf-8')

st.download_button(
    label='Download Customer Priority CSV',
    data=csv_download,
    file_name='filtered_customer_priority.csv',
    mime='text/csv'
)

if 'latitude' in filtered_df.columns and 'longitude' in filtered_df.columns:
    st.subheader('Peta Lokasi Customer')
    map_df = filtered_df[['latitude', 'longitude']].dropna()
    map_df = map_df.rename(columns={'latitude': 'lat', 'longitude': 'lon'})

    if len(map_df) > 0:
        st.map(map_df)
        st.info(make_map_insight(map_df))
    else:
        st.info('Tidak ada data lokasi untuk filter ini.')

st.subheader('CRM Strategy Matrix')
st.dataframe(crm_strategy, use_container_width=True, hide_index=True)
st.info(make_strategy_insight(crm_strategy))

st.caption('Nama pelanggan pada dashboard adalah data dummy untuk kebutuhan simulasi CRM. Nama dummy tidak dipakai sebagai fitur model.')
