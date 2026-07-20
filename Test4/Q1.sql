create database info;
use info;

create table employee(
	employeeid int primary key,
    employeename varchar(500),
    department varchar(500),
    salary int,
    joiningdate date 
);

select * from employee; 