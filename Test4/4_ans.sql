-- Question 4
-- Create the following table.
-- Customer
-- | Column | Data Type |
-- | ------------ | ------------ |
-- | CustomerID | INT |
-- | CustomerName | VARCHAR(100) |
-- | City | VARCHAR(50) |
-- | Mobile | VARCHAR(15) |
-- Tasks
-- 1. Create the table.
-- 2. Make CustomerID the Primary Key.
-- 3. Explain why Primary Keys are important.

CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    City VARCHAR(50),
    Mobile VARCHAR(15)
);

-- PRIMARY KEYS are important because they uniquely identify each record in a table, 
-- And  it doesn't accept duplicate entries or null values.