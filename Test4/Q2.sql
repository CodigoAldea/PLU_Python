create database four;
use four;

create table student(
	Studentid int,
    Name varchar(100),
    Course varchar(100),
    Marks int
);

select * from student;

insert into student (Studentid , Name , Course , Marks)
Values 
	(101 , 'Rahul', 'Python', 80),
	(102 , 'Priya',  'Java',  75),
	(103 , 'Aman' , 'Python', 90), 
	(104 , 'Neha' , 'SQL', 70);

select * from student;

select Name , Marks from student;

select course from student;
