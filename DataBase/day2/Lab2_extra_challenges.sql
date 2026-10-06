---------------EXTRA CHALLENGES------------

---------------LEVEL 1---------------------
---------Excercise 1---------
CREATE TABLE suppliers(
supplier_id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
country TEXT DEFAULT 'Sweden',
email TEXT
);


---------Excercise 2---------
-- When NULL is passed then country is inserted with NULL value
INSERT INTO suppliers(supplier_id,name,country,email)
VALUES(1,'Idax',NULL,'idax@hotmail.com')
;

-- When no value explicitly passed to country then Sweden is inserted
INSERT INTO suppliers(supplier_id,name,email)
VALUES(2,'Madras','madras@gmail.com')
;

SELECT * FROM suppliers;
---------Excercise 3---------
INSERT INTO suppliers(supplier_id,name,country,email)
VALUES(3,'Nordic textiles','Norway','nordictextiles@gmail.com')
;

INSERT INTO suppliers(supplier_id,name,country,email)
VALUES(4,'Nordic textiles','Norway','nordictextiles@gmail.com')
;

-- The above query inserted Duplicate supplier names , since no UNIQUE added to constraint
DROP TABLE suppliers;

CREATE TABLE suppliers(
supplier_id INTEGER PRIMARY KEY,
name TEXT NOT NULL UNIQUE,
country TEXT DEFAULT 'Sweden',
email TEXT
);

INSERT INTO suppliers(supplier_id,name,country,email)
VALUES(3,'Nordic textiles','Norway','nordictextiles@gmail.com')
;

INSERT INTO suppliers(supplier_id,name,country,email)
VALUES(4,'Nordic textiles','Norway','nordictextiles@gmail.com')
;
-- Above insert data failed: UNIQUE constraint failed: suppliers.name

---------Excercise 4---------

CREATE TABLE coupons(
code TEXT PRIMARY KEY,
discount_percent INTEGER NOT NULL CHECK (discount_percent BETWEEN 1 AND 90),
valid_until TEXT NOT NULL
);

-- Inserttion failed with reason - CHECK constraint failed: discount_percent BETWEEN 1 and 90
INSERT INTO coupons(code, discount_percent,valid_until)
VALUES ('SUMMER20', 95, '2026-12-31')
;

--successfully inserted
INSERT INTO coupons(code, discount_percent,valid_until)
VALUES ('SUMMER20', 90, '2026-12-31')
;

-- When column is TEXT SQL lite not automatically assign any values for column is PRIMARY KEY. It shown as NULL
INSERT INTO coupons (discount_percent,valid_until)
VALUES(7,'2026-10-10')
;
---------------LEVEL 2--------------------

---------Excercise 5---------

-- PRIMARY KEY make sure column value unique for each row and NOT NULL
-- In SQL lite if we don't send supplier_id it automatically increment the max(column) for Primary Key
INSERT INTO suppliers(name,country,email)
VALUES ('M texttiles','Finland','mtextiles@gmail.com')
;

---------Excercise 6---------
-- run successfully
ALTER TABLE suppliers
RENAME COLUMN email TO contact_email
;

---------Excercise 7---------
SELECT * FROM sqlite_master;
SELECT name FROM sqlite_master;
SELECT * FROM sqlite_master WHERE type='table';
SELECT * FROM sqlite_master WHERE name='products';

--To view the columns of table 'products'
PRAGMA TABLE_INFO(products);

---------Excercise 8---------

CREATE TABLE product_suppliers(
product_id INTEGER NOT NULL,
supplier_id INTEGER NOT NULL,
purchasing_price NOT NULL CHECK (purchasing_price >0),
PRIMARY KEY (product_id, supplier_id),
FOREIGN KEY(product_id) REFERENCES products(product_id),
FOREIGN KEY(supplier_id) REFERENCES suppliers(supplier_id)
);

---------Excercise 9---------

CREATE TABLE campaigns(
name TEXT PRIMARY KEY,
start_date TEXT NOT NULL ,
end_date TEXT NOT NULL CHECK (start_date < end_date)
);

-- Insert failed. Reason - CHECK constraint failed: start_date < end_date
INSERT INTO campaigns(name,start_date,end_date)
VALUES('AUTUMN25','2026-10-01','2025-10-01');

-- Insert failed. Reason - CHECK constraint failed: start_date < end_date
INSERT INTO campaigns(name,start_date,end_date)
VALUES('AUTUMN25','2026-10-01','2026-10-01');

-- successfully inserted
INSERT INTO campaigns(name,start_date,end_date)
VALUES('AUTUMN25','2026-10-01','2026-11-01');

SELECT * FROM campaigns;


-------------------LEVEL 3--------------------

---------Excercise 10---------

CREATE TABLE product_sizes(
id INTEGER NOT NULL,
product_id INTEGER NOT NULL,
size TEXT NOT NULL CHECK (size IN ('S','M','XL','XXL')),
PRIMARY KEY(id,product_id),
FOREIGN KEY(product_id) REFERENCES products(product_id)
);

INSERT INTO product_sizes(id,product_id,size)
VALUES(1,10,'M');

INSERT INTO product_sizes(id,product_id,size)
VALUES(2,10,'S');

-- Failed to insert: UNIQUE constraint failed: product_sizes.id,product_sizes.product_id
INSERT INTO product_sizes(id,product_id,size)
VALUES(2,10,'M');

---------Excercise 11---------

CREATE TABLE employees(
employee_id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
manager_id INTEGER,
FOREIGN KEY(manager_id) REFERENCES employees(employee_id)

);

DROP TABLE employees;

-- Insert failed- Foreign key mismatch - "employees" referencing "employees"
INSERT INTO employees(employee_id,name,manager_id)
VALUES (11,'sara',1);

-- Insert failed- Foreign key mismatch - "employees" referencing "employees"
INSERT INTO employees(employee_id,name)
VALUES (1,'Bob');

-- Insert successful
INSERT INTO employees(employee_id,name,manager_id)
VALUES (1,'Bob',NULL);

INSERT INTO employees(employee_id,name,manager_id)
VALUES (11,'sara',1);

INSERT INTO employees(employee_id,name,manager_id)
VALUES (5,'Zara',11);

-------------Excercise 12-------------
CREATE TABLE teams(
team_id INTEGER PRIMARY KEY,
name TEXT NOT NULL
);

CREATE TABLE players(
player_id INTEGER NOT NULL,
name TEXT NOT NULL,
team_id INTEGER NOT NULL,
FOREIGN KEY(team_id) REFERENCES teams(team_id)ON DELETE CASCADE,
PRIMARY KEY(player_id,team_id)
);

DROP TABLE teams;
DROP TABLE players;


INSERT INTO teams(team_id,name)
VALUES (1,'TEAM ROCK');

INSERT INTO teams(team_id,name)
VALUES (2,'TEAM ZAG');

INSERT INTO players(player_id,name,team_id)
VALUES(100,'David',1);

INSERT INTO players(player_id,name,team_id)
VALUES(10,'Mia',2);


SELECT * FROM teams;
SELECT * FROM players;

DELETE FROM teams WHERE team_id = 1;

----------------------------------------------------

SELECT * FROM teams;
SELECT * FROM players;