CREATE VIEW HighSalaryEmployees AS
SELECT *
FROM Employee
WHERE Salary > 60000;