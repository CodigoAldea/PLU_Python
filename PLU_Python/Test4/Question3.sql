'''Question 3
Consider the following table.
Product
| ProductID | ProductName | Category | Price |
| --------- | ----------- | ----------- | ----- |
| 1 | Mouse | Electronics | 800 |
| 2 | Laptop | Electronics | 65000 |
| 3 | Chair | Furniture | 4500 |
| 4 | Keyboard | Electronics | 1200 |
Write SQL queries to:
1. Display products costing more than ₹1000.
2. Display all Electronics products.
3. Display the Laptop record'''

-- Here we create table in databseone side we crate table product 
CREATE TABLE Product (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Price INT
);
-- Here we are inserting  data vaules in side table
INSERT INTO Product VALUES
(1,'Mouse','Electronics',800),
(2,'Laptop','Electronics',65000),
(3,'Chair','Furniture',4500),
(4,'Keyboard','Electronics',1200);

-- dispaly electronic records
SELECT *
FROM Product
WHERE Price > 1000;

-- display Laptop records

SELECT *
FROM Product
WHERE ProductName='Laptop';