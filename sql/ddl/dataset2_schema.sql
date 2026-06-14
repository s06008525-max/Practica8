-- DDL Dataset 2: E-commerce normalizado a 3FN

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
