--------------LEVEL 1--------------------

-----Excercise 1----------
SELECT * FROM products WHERE category != 'Accessories' AND stock > 0 AND name LIKE '% %' ORDER BY price DESC;


-----Excercise 2----------
SELECT * FROM customers WHERE city LIKE 'S%' OR city LIKE 'M%' OR city IS NULL;

-----Excercise 3 ---------
SELECT * FROM products ORDER BY price DESC LIMIT 1 OFFSET 1;


-----Excercise 4----------
-- DIFFERENT WAYS--
SELECT * FROM customers WHERE (joined_date > '2023-31-31' AND  joined_date < '2026-01-01') ORDER BY joined_date DESC LIMIT 3;

SELECT * FROM customers WHERE joined_date BETWEEN '2023-31-31' AND '2026-01-01'  ORDER BY joined_date DESC LIMIT 3;

-----ANSWER--CONVERTING TEXT to DATE and compare Year
SELECT * FROM customers WHERE STRFTIME('%Y',joined_date) IN ('2024','2025') ORDER BY joined_date DESC LIMIT 3;


---------------------LEVEL 2----------------------------------------------


-------------Excercise 5----------------
SELECT first_name || ' ' || last_name AS customer_name from customers ORDER BY last_name;

SELECT concat_ws(' ',first_name,last_name) AS customer_name from customers ORDER BY last_name;


-------------Excercise 6-----------------
SELECT name, price,
CASE
 WHEN price < 200 THEN 'budget'
 WHEN price BETWEEN 200 AND 799 THEN 'mild'
 WHEN price >= 800 THEN 'premium'
END as Price_Level
FROM products ORDER BY PRICE;


-----------Excercise 7------------

SELECT first_name, COALESCE(city,'Unknown') AS city FROM customers;

-----------Excercise 8------------
SELECT first_name, STRFTIME('%m',joined_date) FROM customers;
SELECT first_name FROM customers WHERE STRFTIME('%m',joined_date) IN ('01','02','03','04','05','06');
--optimized--
SELECT first_name FROM customers WHERE CAST(STRFTIME('%m',joined_date) AS INTEGER) <= 6;

-----------Excercise 9-----------
SELECT name AS product FROM products ORDER BY LENGTH(name) DESC LIMIT 1;

--optimized--
SELECT name AS prodcut FROM products WHERE LENGTH(name) = (SELECT MAX(LENGTH(name)) FROM products);

----------Excercise 10-----------

SELECT SUBSTR(email,1,(INSTR(email,'@') -1)) FROM customers; -- python equivalent email[0:5]



--------------LEVEL 3------------------

----------Excercise 11-------------

SELECT name AS product FROM products WHERE price > (SELECT AVG(price) FROM products);

----------Excercise 12-------------
-- price Without casting displays as REAL number
SELECT name || ' costs ' || price || 'kr' AS price_list FROM products;

-- price with casting displayed as WHOLE number
SELECT name || ' costs ' || CAST (price AS INTEGER) || 'kr' AS price_list FROM products ORDER BY price;


----------Excercise 13-------------

SELECT city, count(*) from customers GROUP BY city;

----------------------------------------------------