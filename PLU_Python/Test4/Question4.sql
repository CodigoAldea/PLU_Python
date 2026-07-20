'''Question 4
Create the following table.
Customer
| Column | Data Type |
| ------------ | ------------ |
| CustomerID | INT |
| CustomerName | VARCHAR(100) |
| City | VARCHAR(50) |
| Mobile | VARCHAR(15) |
Tasks
1. Create the table.
2. Make CustomerID the Primary Key.
3. Explain why Primary Keys are important.'''

-- here we are creating data table 
CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    City VARCHAR(50),
    Mobile VARCHAR(15)
);


'''Explain why Primary Keys are important.
Primary key: A Primary Key is a column that uniquely identifies each 
record in a table. A primary key cannot contain NULL values and does not allow duplicate values.'''