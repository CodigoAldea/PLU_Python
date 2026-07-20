-- Question 8
-- Consider the following table.
-- Orders
-- | OrderID | CustomerName | OrderDate | Amount |
-- | ------- | ------------ | --------- | ------ |
-- Tasks
-- 1. Create an index on OrderID.
-- 2. Explain one benefit of creating an index.

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    OrderDate DATE,
    Amount DECIMAL(10, 2)
);

CREATE INDEX idx_orderid ON Orders(OrderID);

--index improve the speed of data retrieval and helps in faster search of data from the table. and uses less memory space.