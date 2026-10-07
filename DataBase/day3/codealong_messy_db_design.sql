
CREATE TABLE order_sheet (
  order_no INTEGER,
  customer TEXT,
  email    TEXT,
  city     TEXT,
  products TEXT,
  total    REAL
);
INSERT INTO order_sheet VALUES
(1, 'Anna Lindqvist', 'anna.lindqvist@example.com', 'Uppsala', 'Hoodie Black, Cap Logo x2', 997),
(3, 'Anna Lindqvist', 'anna.lindqvist@example.com', 'Uppsala', 'Socks 3-pack x3', 387),
(4, 'Sara Ahmed', 'sara.ahmed@example.com', 'Goteborg', 'T-shirt White x2, Joggers Grey', 997),
(6, 'Maria Nilsson', 'maria.n@example.com', 'Malmö', 'Hoodie Black, Beanie', 778),
(11, 'Anna Lindqvist', 'anna.l@example.com', 'Uppsala', 'Joggers Grey x2', 998);
 
 
 ----Messy Design---------
 SELECT * FROM order_sheet;

--Return 2 email for the same customer
SELECT DISTINCT email FROM order_sheet WHERE customer = 'Anna Lindqvist';
SELECT DISTINCT city FROM order_sheet;

-- Return products as List
SELECT order_no,products FROM order_sheet WHERE products LIKE '%Joggers%';

-- If one Row name had entered differently then update might be missed
UPDATE order_sheet SET city='Stockholm' WHERE customer='Anna Lindqvist';


------------CORRECT DESIGN------------

UPDATE customers SET city='Stockholm' WHERE customer_id=1;

SELECT order_id,quantity FROM order_items WHERE product_id=6;

