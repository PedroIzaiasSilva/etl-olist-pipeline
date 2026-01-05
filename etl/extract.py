import os
import pandas as pd

# Base paths
RAW_DATA_PATH = 'data/raw/olist'

# Expected files from the Olist dataset
FILES = {
    'orders': 'olist_orders_dataset.csv',
    'customers': 'olist_customers_dataset.csv',
    'order_items': 'olist_order_items_dataset.csv',
    'products': 'olist_products_dataset.csv',
    'payments': 'olist_order_payments_dataset.csv',
}

def check_files_exist():
    '''
    Checks if all expected files exist
    '''

    missing_files = []

    for name, file in FILES.items():
        path = os.path.join(RAW_DATA_PATH, file)
        if not os.path.exists(path):
            missing_files.append(file)

    if missing_files:
        raise FileNotFoundError(
            f'missing files in {RAW_DATA_PATH}: {missing_files}'
        )

def extract():
    """
    Extraction phase:
    - Reads the CSVs
    - Only validates and loads into memory
    """

    print("Starting the EXTRACTION phase")

    check_files_exist()

    dataframes = {}

    for name, file in FILES.items():
        path = os.path.join(RAW_DATA_PATH, file)
        print(f'Reading file: {file}')

        df = pd.read_csv(path)
        dataframes[name] = df

        print(f'{name}: {df.shape[0]} lines | {df.shape[1]} columns')

    print('Extraction completed successfully')
    
    return dataframes

if __name__ == "__main__":
    extract()