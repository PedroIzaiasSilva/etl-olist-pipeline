import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

STAGING_PATH = 'data/staging'
SCHEMA = 'staging'

DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_HOST = os.getenv('POSTGRES_HOST')
DB_PORT = os.getenv('POSTGRES_PORT')
DB_NAME = os.getenv('POSTGRES_DB')

def get_engine():
    connection_string = (
        f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}'
        f'@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    )
    return create_engine(connection_string)


def ensure_schema(engine):
    with engine.connect() as conn:
        conn.execute(
            text(f'CREATE SCHEMA IF NOT EXISTS {SCHEMA}')
        )
        conn.commit()

def load_table(engine, table_name, csv_path):
    print(f'Loading table: {SCHEMA}.{table_name}')

    df = pd.read_csv(csv_path)

    with engine.begin() as conn:
        conn.execute(
            text(f'TRUNCATE TABLE {SCHEMA}.{table_name}')
        )

        df.to_sql(
            table_name,
            conn,
            schema=SCHEMA,
            if_exists='append',
            index=False,
            method='multi',
            chunksize=5000
        )

        print(f'Loaded {len(df)} rows into {table_name}')

def load():
    print('Starting the load phase')

    engine = get_engine()
    ensure_schema(engine)

    for file in os.listdir(STAGING_PATH):
        if file.endswith('.csv'):
            table_name = file.replace('.csv', '')
            csv_path = os.path.join(STAGING_PATH, file)
            load_table(engine, table_name, csv_path)

    print("Load phase completed sucessfully")

if __name__ == '__main__':
    load()