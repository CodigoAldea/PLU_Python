SELECT Employee.Name, Department.DepartmentName
FROM Employee
INNER JOIN Department
ON Employee.DepartmentID = Department.DepartmentID;
