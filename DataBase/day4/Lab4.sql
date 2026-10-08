----------------- LAB4 - JOINING THE TABLES----------------

--------- Excercise 1--------------
--Show every order with the customer's first name, last name and the order status.

SELECT orders.order_id, customers.first_name,customers.last_name
FROM orders 
LEFT JOIN customers ON orders.customer_id = customers.customer_id
;

-- Same result as above query. Just use Alias name for tables to easy to type query 
SELECT o.order_id, c.first_name,c.last_name
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.customer_id
;

--------- Excercise 2--------------
--Show all orders made by Erik.

-- Use JOIN if you need column from multiple tables to be displayed
SELECT o.order_id, CONCAT_WS(' ', c.first_name, c.last_name) AS Name
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.first_name = 'Erik'
;

-- USE sub query only when you need use second table to filter
SELECT order_id,customer_id FROM orders WHERE order_id  IN (
SELECT customer_id FROM customers WHERE first_name='Erik');

--------- Excercise 3--------------
-- Show all orders from customers in Göteborg, newest first.

-- JOIN == INNER JOIN
SELECT o.order_id, c.first_name, c.last_name,c.city
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
WHERE c.city = 'Göteborg'
;

--------- Excercise 4--------------

-- Show every order item with the product name and category

SELECT oi.order_id,p.name,p.category
FROM order_items oi
LEFT JOIN products p ON oi.product_id = p.product_id
;

--------- Excercise 5--------------
-- Which orders contained Shoes? Show order_id and product name.

SELECT oi.order_id,p.name,p.category
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
WHERE p.category = 'Shoes'
;

--------- Excercise 6--------------
--Show the full receipt for order 10: product name, quantity, unit price and line total.

SELECT oi.order_id, p.name AS Product, oi.quantity, oi.unit_price , (oi.quantity * oi.unit_price) AS line_total
FROM order_items oi
LEFT JOIN products p ON oi.product_id = p.product_id
;

--------- Excercise 7--------------
--Show which customers have bought a Hoodie Black (first name and order date).

-- products, customers and order+items tables needs to be joined
SELECT c.first_name, o.order_date
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
JOIN orders o ON oi.order_id = o.order_id
JOIN customers c ON o.customer_id = c.customer_id
WHERE p.name = 'Hoodie Black'
;

--------- Excercise 8--------------
-- Show all customers and their orders, including customers with no orders.

SELECT c.first_name,c.last_name,c.city,o.order_id,o.order_date,o.status
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
;

--------- Excercise 9--------------
SELECT product_id FROM order_items WHERE product_id NOT IN (
SELECT product_id FROM products);

-- Which products have never been sold?
SELECT DISTINCT p.name AS product
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
WHERE oi.product_id IS NULL
;

----- Solve Different way using: EXCEPT
SELECT product_id FROM products
EXCEPT
SELECT product_id FROM order_items;

----- Solve Different way using: NOT EXISTS
SELECT p.product_id,p.name FROM products p
WHERE NOT EXISTS(
SELECT 1 FROM order_items oi WHERE oi.product_id = p.product_id
);

SELECT * FROM products;

--------- Excercise 10--------------
-- customers <-- orders <-- order_items --> products
-- Challenge: show customers from Uppsala and every product they bought (first name, product name, quantity).
SELECT c.first_name, p.name AS product, oi.quantity
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE c.city = 'Uppsala'
;

