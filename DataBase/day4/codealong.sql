SELECT * FROM orders;

SELECT orders.order_id,customers.first_name,orders.order_date
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
;

-- Short name for tables for readability
SELECT o.order_id, c.first_name,o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
;

-- JOIN without ON condition matches every row in orders in orders to customers
-- JOIN == INNER JOIN
SELECT o.order_id, c.first_name, o.order_date
FROM orders o
JOIN customers c
;


-- JOIN with WHERE
-- WHERE will come afetr JOIN
SELECT o.order_id,c.first_name,c.city
FROM orders o
JOIN customers c ON o.order_id = c.customer_id
WHERE c.city = 'Uppsala'
;

-- Order BY with JOIN
SELECT o.order_id, c.first_name,o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
ORDER BY o.order_date DESC
LIMIT 5;

-- JOIN order item with product
SELECT oi.order_id,p.name, oi.quantity
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
;

-- ER diagram
-- customers <-- orders <-- order_items --> products


-- JOIN 4 tables to get customer name, order id, product, quantity
SELECT c.first_name,o.order_date,p.name,oi.quantity
FROM order_items oi
JOIN orders o ON oi.order_id = o.order_id
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON oi.product_id = p.product_id
;


-- LEFT JOIN ( customers has orders)
-- List all customers with and without orders
SELECT c.first_name, o.order_id
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
;

--INNER JOIN
-- returns only matching rows in both tables
SELECT c.first_name, o.order_id
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
;

