'''Question 8
Consider the following table.
Orders
| OrderID | CustomerName | OrderDate | Amount |
| ------- | ------------ | --------- | ------ |
Tasks
1. Create an index on OrderID.
2. Explain one benefit of creating an index'''

-- here we are creating orders datatable inside database
CREATE TABLE Orders (
    OrderID INT,
    CustomerName VARCHAR(100),
    OrderDate DATE,
    Amount INT
);

-- here we are creating indexing for order id printing oder id according to indexing
CREATE INDEX OrderID1
ON Orders(OrderID);



'''2. answer 

An index improves the speed of data retrieval from a 
table. It helps the database find rows more quickly without scanning every record.
and using indexing we easily find'''