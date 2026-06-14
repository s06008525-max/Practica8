import pandas as pd
from sqlalchemy import create_engine, text
import os

DB_URL = 'postgresql://admin:password123@db:5432/db_normalizacion'
engine = create_engine(DB_URL)

DATASETS = {
    'dataset1': {
        'ddl': '/app/sql/ddl/dataset1_schema.sql',
        'tables': ['shows', 'directors', 'actors', 'countries', 'genres', 
                   'show_director', 'show_actor', 'show_country', 'show_genre']
    },
    'dataset2': {
        'ddl': '/app/sql/ddl/dataset2_schema.sql',
        'tables': ['customers', 'products', 'invoices', 'invoice_details']
    },
    'dataset3': {
        'ddl': '/app/sql/ddl/dataset3_schema.sql',
        'tables': ['patients', 'icus', 'encounters']
    }
}

RENAME_MAP = {
    'CustomerID': 'customer_id',
    'Country': 'country',
    'StockCode': 'stock_code',
    'Description': 'description',
    'InvoiceNo': 'invoice_no',
    'InvoiceDate': 'invoice_date',
    'Quantity': 'quantity',
    'UnitPrice': 'unit_price',
    'DetailID': 'detail_id'
}

def load_all_to_postgres():
    print("conexión PostgreSQL")
    
    with engine.connect() as connection:
        for ds_name, config in DATASETS.items():
            print(f"\n- Procesando {ds_name.upper()}")
            
            print("tablas parciales")
            for table in config['tables']:
                connection.execute(text(f"DROP TABLE IF EXISTS {table} CASCADE;"))
            connection.commit()
            
            print(f"Ejec DDL: {config['ddl']}...")
            with open(config['ddl'], 'r', encoding='utf-8') as file:
                ddl_commands = file.read()
                for cmd in ddl_commands.split(';'):
                    if cmd.strip():
                        connection.execute(text(cmd))
            connection.commit()
            
            print("Insert datos en CSVs")
            for table in config['tables']:
                csv_path = f'/app/data/normalized/{ds_name}/{table}.csv'
                if os.path.exists(csv_path):
                    print(f" - tabla '{table}'...")
                    
                    df = pd.read_csv(csv_path)
                    
                    df = df.rename(columns=RENAME_MAP)
                    
                    for col in df.columns:
                        if df[col].dtype == 'object':
                            df[col] = df[col].fillna('Unknown')
                            
                    df = df.drop_duplicates()
                    
                    df.to_sql(table, con=engine, if_exists='append', index=False)
                    
                    generate_dml_sample(table, df, ds_name)

def generate_dml_sample(table_name, df, ds_name):
    dml_dir = '/app/sql/dml/'
    os.makedirs(dml_dir, exist_ok=True)
    dml_file = os.path.join(dml_dir, f'{ds_name}_data.sql')
    
    sample_df = df.head(5)
    
    with open(dml_file, 'a', encoding='utf-8') as f:
        f.write(f"\n- INSERTS tabla {table_name}\n")
        for index, row in sample_df.iterrows():
            cols = ', '.join(str(i) for i in row.index.tolist())
            vals = ', '.join(f"'{str(x).replace(chr(39), chr(39)+chr(39))}'" if pd.notnull(x) else 'NULL' for x in row.values)
            insert_stmt = f"INSERT INTO {table_name} ({cols}) VALUES ({vals});\n"
            f.write(insert_stmt)

if __name__ == '__main__':
    try:
        load_all_to_postgres()
        print("\npostgres correcto")
    except Exception as e:
        print(f"\nerror: {e}")