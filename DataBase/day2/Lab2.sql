-----------------LAB 2------------------

---------Excercise 1---------
CREATE TABLE books(
book_id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
author TEXT,
year INTEGER
);

---------Excercise 2---------
DROP TABLE books;

CREATE TABLE books(
book_id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
author TEXT,
year INTEGER CHECK (year>1400)
);
---------Excercise 3---------

ALTER TABLE books
ADD COLUMN isbn TEXT
;
---------Excercise 4---------
DELETE FROM books;

---------Excercise 5---------

CREATE TABLE reviews(
review_id INTEGER PRIMARY KEY,
product_id INTEGER NOT NULL,
rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
comment TEXT,
FOREIGN KEY(product_id) REFERENCES products(product_id)
);

---------Excercise 6---------
-- When tried to insert CHECK constraint alarmed that rating Should be BETWEEN 1 AND 5
INSERT INTO reviews(review_id, product_id,rating)
VALUES(10,12,6)
;

---------Excercise 7---------

-- When tried with product id 50 FOREIGN KEY constraint falied
INSERT INTO reviews(review_id, product_id,rating)
VALUES(10,50,3)
;
