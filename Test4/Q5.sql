create database seven;
use seven;

create table Employee(
	EmployeeId int,
    Name varchar(100),
    DepartmentId int
);

insert into Employee(EmployeeId, Name , DepartmentId) 
values
	(1 ,'Rahul', 101),
	(2 ,'Priya' ,102),
	(3 ,'Aman',  101);
    
create table Department(
	DepartmentId int,
    Departname varchar(100)
);

insert into Department(DepartmentId , Departname)
values
	( 101 , 'IT'),
	(102 , 'HR');

select Name from Employee;

select Departname from Department;

select Employee.Name, Department.Departname
from employee
inner join Department
on employee.DepartmentId = Department.DepartmentId;