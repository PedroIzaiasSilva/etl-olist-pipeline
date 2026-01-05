import os
import pandas as pd
from extract import extract

STAGING_PATH = 'data/staging'

def ensure_staging_path():
    os.makedirs(STAGING_PATH, exist_ok=True)

def transform_orders(df):
    df = df.copy()

    # Datas
    date_columns = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]

    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

    #Remove duplicate
    df = df.drop_duplicates(subset=['order_id'])

    return df

def transform_customers(df):
    df = df.copy()

    df = df.drop_duplicates(subset=['customer_id'])

    return df

def transform_order_items(df):
    df = df.copy()

    df['shipping_limit_date'] = pd.to_datetime(
        df['shipping_limit_date'], errors='coerce'
    )

    return df

def transform_products(df):
    df = df.copy()

    df = df.drop_duplicates(subset=['product_id'])

    return df

def transform_payments(df):
    df = df.copy()

    return df

def transform():
    print('Starting the TRANSFORM phase')

    ensure_staging_path()

    dfs = extract()

    transformed = {
        'orders': transform_orders(dfs['orders']),
        'customers': transform_customers(dfs['customers']),
        'order_items': transform_order_items(dfs['order_items']),
        'products': transform_products(dfs['products']),
        'payments': transform_payments(dfs['payments']),
    }

    for name, df in transformed.items():
        output_path = os.path.join(STAGING_PATH, f'{name}.csv')
        df.to_csv(output_path, index=False)
        print(f'Save staging file: {output_path}')

    print('Transform phase completed successfully')

if __name__ == "__main__":
    transform()