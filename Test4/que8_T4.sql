CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    OrderDate DATE,
    Amount DECIMAL(10, 2)
);

CREATE INDEX idx_orderid ON Orders(OrderID);

--index improve the speed of data retrieval and helps in faster search of data from the table. 