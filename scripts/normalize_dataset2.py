import pandas as pd
import os

RAW_FILE = '/app/data/raw/data.csv'
NORM_DIR = '/app/data/normalized/dataset2/'
DDL_FILE = '/app/sql/ddl/dataset2_schema.sql'

os.makedirs(NORM_DIR, exist_ok=True)
os.makedirs(os.path.dirname(DDL_FILE), exist_ok=True)

print("Normalización E-commerce Dataset 2 (data)")
df = pd.read_csv(RAW_FILE, encoding='unicode_escape')

print("Limpiar valores nulos y estandarizar")
df['CustomerID'] = df['CustomerID'].fillna(99999).astype(int)
df['Description'] = df['Description'].fillna('Unknown')

print("1. tabla de Clientes (Customers): Un cliente solo debe tener registrado su país una vez (3FN)")
customers_df = df[['CustomerID', 'Country']].drop_duplicates(subset=['CustomerID']).copy()

print("2. tabla de Productos (Products): Un código de stock solo debe tener su descripción una vez (2FN)")
products_df = df[['StockCode', 'Description']].drop_duplicates(subset=['StockCode']).copy()

print("3. tabla de Facturas (Invoices): la factura tiene la fecha y quién compró")
invoices_df = df[['InvoiceNo', 'InvoiceDate', 'CustomerID']].drop_duplicates(subset=['InvoiceNo']).copy()

print("4. tabla de Detalles de Factura (Invoice_Details): conecta la factura con el producto, cantidad y precio unitario")
details_df = df[['InvoiceNo', 'StockCode', 'Quantity', 'UnitPrice']].copy()
details_df['DetailID'] = range(1, len(details_df) + 1)

print("Export CSVs data/normalized/dataset2")
customers_df.to_csv(os.path.join(NORM_DIR, 'customers.csv'), index=False)
products_df.to_csv(os.path.join(NORM_DIR, 'products.csv'), index=False)
invoices_df.to_csv(os.path.join(NORM_DIR, 'invoices.csv'), index=False)
details_df.to_csv(os.path.join(NORM_DIR, 'invoice_details.csv'), index=False)

print("script DDL de SQL")
ddl_script = """-- DDL Dataset 2: E-commerce normalizado a 3FN

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    country VARCHAR(100)
);

CREATE TABLE products (
    stock_code VARCHAR(50) PRIMARY KEY,
    description TEXT
);

CREATE TABLE invoices (
    invoice_no VARCHAR(50) PRIMARY KEY,
    invoice_date VARCHAR(50),
    customer_id INT REFERENCES customers(customer_id)
);

CREATE TABLE invoice_details (
    detail_id SERIAL PRIMARY KEY,
    invoice_no VARCHAR(50) REFERENCES invoices(invoice_no),
    stock_code VARCHAR(50) REFERENCES products(stock_code),
    quantity INT,
    unit_price DECIMAL(10, 2)
);
"""

with open(DDL_FILE, 'w', encoding='utf-8') as f:
    f.write(ddl_script)

print("\nE-commerce normalizado 'normalized/dataset2' y 'sql/ddl'.")