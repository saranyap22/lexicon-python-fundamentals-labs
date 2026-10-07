----------------LAB 3----------------
SELECT * FROM orders;

-------- Excercise 1---------------
SELECT * FROM customers;

INSERT INTO customers(customer_id, first_name,last_name,email,city,joined_date)
VALUES (11,'Saranya','Palanisamy','sara@gmail.com','solna','2026-10-07');


-------- Excercise 2---------------
SELECT * FROM products;
INSERT INTO products(name,category,price,stock)
VALUES ('Scarf','Accessories',229,15),('Gloves','Accessories',199,20);

-------- Excercise 3---------------
SELECT * FROM orders WHERE order_id = 16;
SELECT * FROM order_items WHERE order_id=16;

INSERT INTO orders(order_id,customer_id,order_date)
VALUES (16,7,'2026-10-07');

INSERT INTO order_items(order_id,product_id,quantity,unit_price)
VALUES (16,10,2,179);
-------- Excercise 4---------------
-- Results: CHECK constraint failed: quantity > 0
INSERT INTO order_items(order_id,product_id,quantity,unit_price)
VALUES (16,11,0,100)
;

-------- Excercise 5---------------
SELECT DISTINCT status FROM orders;
SELECT * FROM orders WHERE order_id=12;
UPDATE orders SET status='shipped' WHERE order_id=12;

-------- Excercise 6---------------
SELECT * FROM products WHERE product_id = 5;

UPDATE products SET stock=50 WHERE product_id = 5;

-------- Excercise 7---------------

SELECT name,price FROM products WHERE category='Accessories';

UPDATE products SET price = price * 1.1 WHERE category='Accessories';

-------- Excercise 8---------------
SELECT order_id FROM orders WHERE status = 'cancelled';
SELECT * FROM order_items;

-- Cannot Delete without deleting order_items relates to order_id to be deleted. Foreign Key constraint
DELETE FROM orders WHERE status = 'cancelled';

DELETE FROM order_items WHERE order_id IN (SELECT order_id FROM orders WHERE status = 'cancelled');
DELETE FROM orders WHERE status = 'cancelled';

-------- Excercise 9---------------
-- After Revert changes
SELECT COUNT(*) FROM orders;

------------------------------------