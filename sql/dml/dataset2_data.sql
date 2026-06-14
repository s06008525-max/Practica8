
- INSERTS tabla customers
INSERT INTO customers (customer_id, country) VALUES ('17850', 'United Kingdom');
INSERT INTO customers (customer_id, country) VALUES ('13047', 'United Kingdom');
INSERT INTO customers (customer_id, country) VALUES ('12583', 'France');
INSERT INTO customers (customer_id, country) VALUES ('13748', 'United Kingdom');
INSERT INTO customers (customer_id, country) VALUES ('15100', 'United Kingdom');

- INSERTS tabla products
INSERT INTO products (stock_code, description) VALUES ('85123A', 'WHITE HANGING HEART T-LIGHT HOLDER');
INSERT INTO products (stock_code, description) VALUES ('71053', 'WHITE METAL LANTERN');
INSERT INTO products (stock_code, description) VALUES ('84406B', 'CREAM CUPID HEARTS COAT HANGER');
INSERT INTO products (stock_code, description) VALUES ('84029G', 'KNITTED UNION FLAG HOT WATER BOTTLE');
INSERT INTO products (stock_code, description) VALUES ('84029E', 'RED WOOLLY HOTTIE WHITE HEART.');

- INSERTS tabla invoices
INSERT INTO invoices (invoice_no, invoice_date, customer_id) VALUES ('536365', '12/1/2010 8:26', '17850');
INSERT INTO invoices (invoice_no, invoice_date, customer_id) VALUES ('536366', '12/1/2010 8:28', '17850');
INSERT INTO invoices (invoice_no, invoice_date, customer_id) VALUES ('536367', '12/1/2010 8:34', '13047');
INSERT INTO invoices (invoice_no, invoice_date, customer_id) VALUES ('536368', '12/1/2010 8:34', '13047');
INSERT INTO invoices (invoice_no, invoice_date, customer_id) VALUES ('536369', '12/1/2010 8:35', '13047');

- INSERTS tabla invoice_details
INSERT INTO invoice_details (invoice_no, stock_code, quantity, unit_price, detail_id) VALUES ('536365', '85123A', '6', '2.55', '1');
INSERT INTO invoice_details (invoice_no, stock_code, quantity, unit_price, detail_id) VALUES ('536365', '71053', '6', '3.39', '2');
INSERT INTO invoice_details (invoice_no, stock_code, quantity, unit_price, detail_id) VALUES ('536365', '84406B', '8', '2.75', '3');
INSERT INTO invoice_details (invoice_no, stock_code, quantity, unit_price, detail_id) VALUES ('536365', '84029G', '6', '3.39', '4');
INSERT INTO invoice_details (invoice_no, stock_code, quantity, unit_price, detail_id) VALUES ('536365', '84029E', '6', '3.39', '5');
