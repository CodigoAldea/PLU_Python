'''Question 7
Consider the following table.
Employee
| EmployeeID | Name | Department | Salary |
| ---------- | ----- | ---------- | ------ |
| 1 | Rahul | IT | 65000 |
| 2 | Priya | HR | 45000 |
| 3 | Aman | IT | 70000 |
Create a view named `HighSalaryEmployees` that displays employees earning
more than ₹60,000.'''

-- here we are creating employee table
CREATE TABLE Employee (
    EmployeeID INT,
    Name VARCHAR(50),
    Department VARCHAR(50),
    Salary INT
);
-- insertting data in employee table
INSERT INTO Employee VALUES
(1,'Rahul','IT',65000),
(2,'Priya','HR',45000),
(3,'Aman','IT',70000);
-- here we are creating view name for view highsalaryemployee
CREATE VIEW HighSalaryEmployees AS
SELECT *FROM Employee
WHERE Salary>60000;

-- here displying higher  salary employee
SELECT * FROM HighSalaryEmployees;