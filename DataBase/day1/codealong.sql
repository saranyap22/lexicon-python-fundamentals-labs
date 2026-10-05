-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT first_name, last_name, city from customers;
-- Result: 10 rows returned in 10ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT frst_name, last_name, city from customers;
-- Result: no such column: frst_name
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT first_name, last_name, city from customers;
-- Result: 10 rows returned in 7ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT first_name last_name, city from customers;
-- Result: 10 rows returned in 9ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT first_name last_name city
-- Result: near "city": syntax error
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT first_name last_name, city from customers;
-- Result: 10 rows returned in 6ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT first_name, last_name city from customers;
-- Result: 10 rows returned in 5ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT * from products;
-- Result: 12 rows returned in 13ms
-- At line 3:
SELECT first_name, last_name, city from customers;
-- Result: 10 rows returned in 11ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT * from products;
-- Result: 12 rows returned in 9ms
-- At line 3:
SELECT first_name, last_name, city from customers;
-- Result: 10 rows returned in 11ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT first_name, last_name, city from customers;
-- Result: 10 rows returned in 10ms
-- At line 3:
SELECT * from products;
-- Result: 12 rows returned in 10ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 3:
SELECT * from products;
-- Result: 12 rows returned in 10ms
-- At line 5:
SELECT first_name, last_name, city from customers
WHERE city= 'uppsala';
-- Result: 0 rows returned in 8ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 3:
SELECT * from products;
-- Result: 12 rows returned in 12ms
-- At line 5:
SELECT first_name, last_name, city from customers
WHERE city= 'Uppsala';
-- Result: 3 rows returned in 12ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 3:
SELECT * from products;
-- Result: 12 rows returned in 9ms
-- At line 5:
SELECT first_name, last_name, city from customers;
-- Result: 10 rows returned in 11ms
-- At line 6:
SELECT * from customers
WHERE city= Uppsala;
-- Result: no such column: Uppsala
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 3:
SELECT * from products;
-- Result: 12 rows returned in 11ms
-- At line 5:
SELECT first_name, last_name, city from customers;
-- Result: 10 rows returned in 11ms
-- At line 6:
SELECT * from customers
WHERE city= 'Uppsala';
-- Result: 3 rows returned in 11ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELCT
-- Result: near "SELCT": syntax error
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT name. price from products WHERE price < 500
-- Result: no such column: name.price
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT name. price FROM products WHERE price < 500
-- Result: no such column: name.price
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT name. price FROM products WHERE price < 500;
-- Result: no such column: name.price
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT name. price FROM products WHERE price < 500;
-- Result: no such column: name.price
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT name, price FROM products WHERE price < 500;
-- Result: 7 rows returned in 8ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT name,category, price FROM products WHERE category='Shoes' OR category='Accessories';
-- Result: 7 rows returned in 10ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT name, category FROM products WHERE category in ('Shoes','Accessories');
-- Result: 7 rows returned in 7ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT name, price FROM products WHERE price >200 and price <500
-- Result: 3 rows returned in 5ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT name, price FROM products WHERE price BETWEEN 200 AND 400;
-- Result: 2 rows returned in 8ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT name, price FROM products WHERE name 'S%'
-- Result: near "'S%'": syntax error
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT name, price FROM products WHERE name LIKE 'S%'
-- Result: 3 rows returned in 8ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT name, price FROM products WHERE name LIKE 'S%'

SELECT
-- Result: near "SELECT": syntax error
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT name, price FROM products WHERE name LIKE 'S%';
-- Result: 3 rows returned in 8ms
-- At line 3:
SELECT first_name,joined_date FROM customers 
WHERE joined_date > '2025-01-01'
-- Result: 4 rows returned in 11ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT name, price FROM products WHERE name LIKE 'S%';
-- Result: 3 rows returned in 6ms
-- At line 3:
SELECT first_name,joined_date FROM customers 
WHERE joined_date >= '2025-01-01'
-- Result: 4 rows returned in 9ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT first_name,last_name,city from customers;
-- Result: 10 rows returned in 9ms
-- At line 3:
SELECT first_name,joined_date FROM customers 
WHERE joined_date >= '2025-01-01'
-- Result: 4 rows returned in 9ms
-- EXECUTING SELECTION IN 'SQL 1*'
--
-- At line 1:
SELECT first_name,last_name,city from customers;
-- Result: 10 rows returned in 13ms
-- EXECUTING SELECTION IN 'SQL 1*'
--
-- At line 1:
SELECT first_name,last_name,city from customers;
-- Result: 10 rows returned in 7ms
-- At line 3:
SELECT first_name,joined_date FROM customers 
WHERE joined_date >= '2025-01-01';
-- Result: 4 rows returned in 9ms
-- EXECUTING SELECTION IN 'SQL 1*'
--
-- At line 7:
SELECT name, price FROM products ORDER BY price DESC;
-- Result: 12 rows returned in 9ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT first_name,last_name,city from customers;
-- Result: 10 rows returned in 8ms
-- At line 3:
SELECT first_name,joined_date FROM customers 
WHERE joined_date >= '2025-01-01';
-- Result: 4 rows returned in 10ms
-- At line 7:
SELECT name, price FROM products ORDER BY price;
-- Result: 12 rows returned in 8ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT first_name,last_name,city from customers;
-- Result: 10 rows returned in 10ms
-- At line 3:
SELECT first_name,joined_date FROM customers 
WHERE joined_date >= '2025-01-01';
-- Result: 4 rows returned in 10ms
-- At line 7:
SELECT name, price FROM products ORDER BY price ASC;
-- Result: 12 rows returned in 6ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT first_name,last_name,city from customers;
-- Result: 10 rows returned in 9ms
-- At line 3:
SELECT first_name,joined_date FROM customers 
WHERE joined_date >= '2025-01-01';
-- Result: 4 rows returned in 9ms
-- At line 7:
SELECT name, price FROM products ORDER BY price;
-- Result: 12 rows returned in 7ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT first_name,last_name,city from customers;
-- Result: 10 rows returned in 11ms
-- At line 3:
SELECT first_name,joined_date FROM customers 
WHERE joined_date >= '2025-01-01';
-- Result: 4 rows returned in 9ms
-- At line 7:
SELECT name, price FROM products ORDER BY price ASC;
-- Result: 12 rows returned in 7ms
-- At line 8:
SELECT name, price FROM products ORDER BY price DESC;
-- Result: 12 rows returned in 9ms
-- At line 9:
SELECT name, price FROM products ORDER BY price;
-- Result: 12 rows returned in 7ms
-- At line 11:
SELECT name, price FROM products ORDER BY price ASC LIMIT 3;
-- Result: 3 rows returned in 6ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT first_name,last_name,city from customers;
-- Result: 10 rows returned in 9ms
-- At line 3:
SELECT first_name,joined_date FROM customers 
WHERE joined_date >= '2025-01-01';
-- Result: 4 rows returned in 10ms
-- At line 7:
SELECT name, price FROM products ORDER BY price ASC;
-- Result: 12 rows returned in 6ms
-- At line 8:
SELECT name, price FROM products ORDER BY price DESC;
-- Result: 12 rows returned in 7ms
-- At line 9:
SELECT name, price FROM products ORDER BY price;
-- Result: 12 rows returned in 7ms
-- At line 11:
SELECT name, price FROM products ORDER BY price DESC LIMIT 3;
-- Result: 3 rows returned in 6ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT first_name,last_name,city from customers;
-- Result: 10 rows returned in 8ms
-- At line 3:
SELECT first_name,joined_date FROM customers 
WHERE joined_date >= '2025-01-01';
-- Result: 4 rows returned in 9ms
-- At line 7:
SELECT name, price FROM products ORDER BY price ASC;
-- Result: 12 rows returned in 7ms
-- At line 8:
SELECT name, price FROM products ORDER BY price DESC;
-- Result: 12 rows returned in 6ms
-- At line 9:
SELECT name, price FROM products ORDER BY price;
-- Result: 12 rows returned in 7ms
-- At line 11:
SELECT name, price FROM products ORDER BY price DESC LIMIT 3;
-- Result: 3 rows returned in 6ms
-- At line 13:
SELECT DISTINCT city from customers;
-- Result: 6 rows returned in 6ms
-- EXECUTING SELECTION IN 'SQL 1*'
--
-- At line 13:
SELECT city from customers;
-- Result: 10 rows returned in 7ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT first_name,last_name,city from customers;
-- Result: 10 rows returned in 8ms
-- At line 3:
SELECT first_name,joined_date FROM customers 
WHERE joined_date >= '2025-01-01';
-- Result: 4 rows returned in 9ms
-- At line 7:
SELECT name, price FROM products ORDER BY price ASC;
-- Result: 12 rows returned in 7ms
-- At line 8:
SELECT name, price FROM products ORDER BY price DESC;
-- Result: 12 rows returned in 7ms
-- At line 9:
SELECT name, price FROM products ORDER BY price;
-- Result: 12 rows returned in 7ms
-- At line 11:
SELECT name, price FROM products ORDER BY price DESC LIMIT 3;
-- Result: 3 rows returned in 7ms
-- At line 13:
SELECT city from customers;
-- Result: 10 rows returned in 7ms
-- At line 14:
SELECT DISTINCT city from customers;
-- Result: 6 rows returned in 6ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT first_name,last_name,city from customers;
-- Result: 10 rows returned in 10ms
-- At line 3:
SELECT first_name,joined_date FROM customers 
WHERE joined_date >= '2025-01-01';
-- Result: 4 rows returned in 10ms
-- At line 7:
SELECT name, price FROM products ORDER BY price ASC;
-- Result: 12 rows returned in 7ms
-- At line 8:
SELECT name, price FROM products ORDER BY price DESC;
-- Result: 12 rows returned in 8ms
-- At line 9:
SELECT name, price FROM products ORDER BY price;
-- Result: 12 rows returned in 7ms
-- At line 11:
SELECT name, price FROM products ORDER BY price DESC LIMIT 3;
-- Result: 3 rows returned in 6ms
-- At line 13:
SELECT city from customers;
-- Result: 10 rows returned in 7ms
-- At line 14:
SELECT DISTINCT city from customers;
-- Result: 6 rows returned in 6ms
-- At line 17:
SELECT name AS product, price AS price_sek FROM products;
-- Result: 12 rows returned in 6ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT first_name,last_name,city from customers;
-- Result: 10 rows returned in 8ms
-- At line 3:
SELECT first_name,joined_date FROM customers 
WHERE joined_date >= '2025-01-01';
-- Result: 4 rows returned in 9ms
-- At line 7:
SELECT name, price FROM products ORDER BY price ASC;
-- Result: 12 rows returned in 6ms
-- At line 8:
SELECT name, price FROM products ORDER BY price DESC;
-- Result: 12 rows returned in 7ms
-- At line 9:
SELECT name, price FROM products ORDER BY price;
-- Result: 12 rows returned in 6ms
-- At line 11:
SELECT name, price FROM products ORDER BY price DESC LIMIT 3;
-- Result: 3 rows returned in 6ms
-- At line 13:
SELECT city from customers;
-- Result: 10 rows returned in 7ms
-- At line 14:
SELECT DISTINCT city from customers;
-- Result: 6 rows returned in 6ms
-- At line 17:
SELECT name AS product, price AS price_sek FROM products;
-- Result: 12 rows returned in 7ms
-- At line 18:
SELECT * from customers WHERE city=NULL
-- Result: 0 rows returned in 6ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT first_name,last_name,city from customers;
-- Result: 10 rows returned in 11ms
-- At line 3:
SELECT first_name,joined_date FROM customers 
WHERE joined_date >= '2025-01-01';
-- Result: 4 rows returned in 8ms
-- At line 7:
SELECT name, price FROM products ORDER BY price ASC;
-- Result: 12 rows returned in 7ms
-- At line 8:
SELECT name, price FROM products ORDER BY price DESC;
-- Result: 12 rows returned in 7ms
-- At line 9:
SELECT name, price FROM products ORDER BY price;
-- Result: 12 rows returned in 7ms
-- At line 11:
SELECT name, price FROM products ORDER BY price DESC LIMIT 3;
-- Result: 3 rows returned in 6ms
-- At line 13:
SELECT city from customers;
-- Result: 10 rows returned in 5ms
-- At line 14:
SELECT DISTINCT city from customers;
-- Result: 6 rows returned in 6ms
-- At line 17:
SELECT name AS product, price AS price_sek FROM products;
-- Result: 12 rows returned in 6ms
-- At line 18:
SELECT * from customers WHERE city='NULL'
-- Result: 0 rows returned in 6ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT first_name,last_name,city from customers;
-- Result: 10 rows returned in 9ms
-- At line 3:
SELECT first_name,joined_date FROM customers 
WHERE joined_date >= '2025-01-01';
-- Result: 4 rows returned in 9ms
-- At line 7:
SELECT name, price FROM products ORDER BY price ASC;
-- Result: 12 rows returned in 7ms
-- At line 8:
SELECT name, price FROM products ORDER BY price DESC;
-- Result: 12 rows returned in 7ms
-- At line 9:
SELECT name, price FROM products ORDER BY price;
-- Result: 12 rows returned in 6ms
-- At line 11:
SELECT name, price FROM products ORDER BY price DESC LIMIT 3;
-- Result: 3 rows returned in 6ms
-- At line 13:
SELECT city from customers;
-- Result: 10 rows returned in 5ms
-- At line 14:
SELECT DISTINCT city from customers;
-- Result: 6 rows returned in 7ms
-- At line 17:
SELECT name AS product, price AS price_sek FROM products;
-- Result: 12 rows returned in 6ms
-- At line 18:
SELECT * from customers WHERE city=NULL;
-- Result: 0 rows returned in 6ms
-- At line 20:
SELECT * from customers WHERE city IS NULL;
-- Result: 1 rows returned in 7ms
-- EXECUTING ALL IN 'SQL 1*'
--
-- At line 1:
SELECT first_name,last_name,city from customers;
-- Result: 10 rows returned in 8ms
-- At line 3:
SELECT first_name,joined_date FROM customers 
WHERE joined_date >= '2025-01-01';
-- Result: 4 rows returned in 11ms
-- At line 7:
SELECT name, price FROM products ORDER BY price ASC;
-- Result: 12 rows returned in 6ms
-- At line 8:
SELECT name, price FROM products ORDER BY price DESC;
-- Result: 12 rows returned in 9ms
-- At line 9:
SELECT name, price FROM products ORDER BY price;
-- Result: 12 rows returned in 7ms
-- At line 11:
SELECT name, price FROM products ORDER BY price DESC LIMIT 3;
-- Result: 3 rows returned in 6ms
-- At line 13:
SELECT city from customers;
-- Result: 10 rows returned in 6ms
-- At line 14:
SELECT DISTINCT city from customers;
-- Result: 6 rows returned in 6ms
-- At line 17:
SELECT name AS product, price AS price_sek FROM products;
-- Result: 12 rows returned in 6ms
-- At line 18:
SELECT * from customers WHERE city=NULL;
-- Result: 0 rows returned in 6ms
-- At line 20:
SELECT * from customers WHERE city IS NULL;
-- Result: 1 rows returned in 6ms
-- At line 21:
