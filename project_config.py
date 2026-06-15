
from pathlib import Path

PROJECT_DIR = Path(r'/content/drive/MyDrive/Proyek_CRM_KELOMPOK')
RAW_DIR = PROJECT_DIR / 'data' / 'raw'
PROCESSED_DIR = PROJECT_DIR / 'data' / 'processed'
NOTEBOOK_DIR = PROJECT_DIR / 'notebooks'
OUTPUT_DIR = PROJECT_DIR / 'outputs'
REPORT_DIR = PROJECT_DIR / 'reports'

RAW_DATA_PATH = RAW_DIR / 'onlinedeliverydata.csv'
CLEAN_DATA_PATH = PROCESSED_DIR / 'online_delivery_clean.csv'
FINAL_DATA_PATH = PROCESSED_DIR / 'food_delivery_crm_final_result.csv'
