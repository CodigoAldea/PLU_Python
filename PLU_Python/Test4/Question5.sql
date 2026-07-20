'''Question 5
Consider the following tables.
Employee
| EmployeeID | Name | DepartmentID |
| ---------- | ----- | ------------ |
| 1 | Rahul | 101 |
| 2 | Priya | 102 |
| 3 | Aman | 101 |
Department
| DepartmentID | DepartmentName |
| ------------ | -------------- |
| 101 | IT |
| 102 | HR |
Write an SQL query to display
* Employee Name
* Department Name
using an INNER JOIN.'''

-- here creating datatable EmployeeJoin 
CREATE TABLE Employee (
    EmployeeID INT,
    Name VARCHAR(50),
    DepartmentID INT
);

-- here we insert data values in side table 
INSERT INTO Employee VALUES
(1,'Rahul',101),
(2,'Priya',102),
(3,'Aman',101);


-- here creating new data table Dpartment and departmentID as primary key
CREATE TABLE Department (
    DepartmentID INT,
    DepartmentName VARCHAR(50)
);

INSERT INTO Department VALUES
(101,'IT'),
(102,'HR');

-- INNER joing here Employee and  department using inner join
SELECT
Employee.Name,
Department.Department
FROM Employee
INNER JOIN Department
ON Employee.DepartmentID=Department.DepartmentID;