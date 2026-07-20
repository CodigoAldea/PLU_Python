create database eight;
use eight;

create table student(
	studentid int,
    name varchar(100),
    courseid int);

select * from student;

insert into student(studentid , name , courseid)
values
	(1 , 'Rahul' , 201),
    (2 , 'Neha' , 202),
    (3 ,  'Aman' , Null);

create table course(
	courseid int,
    coursename varchar(100)
);

insert into course(courseid , coursename)
values
	(201 , 'Python'),
	(202 , 'SQL');
    
select student.name, course.coursename 
from student
left join course 
on student.courseid = course.courseid; 