create database nine;
use nine;

create table employee(
	employeeid int,
	name varchar(100),
    department varchar(100),
    salary int
);

insert into employee(employeeid , name , department , salary)
values
	( 1 , 'Rahul' ,'IT' , 65000),
	( 2 , 'Priya' , 'HR' , 45000),
	( 3 , 'Aman' , 'IT' , 70000);

select * from employee;

create view highsalaryemployee as
select * from employee where salary > 60000;
select * from highsalaryemployee;