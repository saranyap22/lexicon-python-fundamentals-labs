CREATE TABLE pets(
pet_id  INTEGER PRIMARY_KEY,
name TEXT,
species TEXT,
age INTEGER

);


INSERT INTO pets VALUES(1,'Bella','dog',3);
SELECT * FROM pets;

INSERT INTO pets VALUES(2,NULL,'cat',-5);
SELECT * FROM pets;

-- Alter table add column and have NULL as default value for all the rows
ALTER TABLE pets ADD COLUMN owner TEXT;

-- Table built without rules is not correct
DROP TABLE pets;

-- Create table with proper rules
CREATE TABLE pets(
pet_id INTEGER PRIMARY_KEY,
name TEXT NOT NULL,
species TEXT NOT NULL,
age INTEGER CHECK (age >= 0),
vaccinated INTEGER DEFAULT 0
);

-- Failed with contraint errors
INSERT INTO pets(pet_id,name,species,age,vaccinated) 
VALUES(2,NULL,'cat',6,1);
INSERT INTO pets(pet_id,name,species,age) 
VALUES(2,'Jin','cat',1);

SELECT * FROM pets;

DROP TABLE pets;

--------------------------------------------------

CREATE TABLE orders(
order_id INTEGER PRIMARY KEY,
customer_id INTEGER NOT NULL,
order_date TEXT NOT NULL,
status TEXT NOT NULL DEFAULT 'new'
		CHECK(status IN ('new','shipped','delivered','cancelled')),
FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items(
order_id INTEGER NOT NULL,
product_id INTEGER NOT NULL,
quantity INTEGER NOT NULL CHECK (quantity > 0),
unit_price REAL NOT NULL,
PRIMARY KEY (order_id,product_id),
FOREIGN KEY (order_id) REFERENCES orders(order_id)
FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Here below script fails because 
-- Foreign key constraint check for customer_id automatically cross check if customer exists in customers table
INSERT INTO orders(order_id,customer_id,order_date)
VALUES(100,999,'2026-10-01');
