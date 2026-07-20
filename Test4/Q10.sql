create database twelve;
use twelve;

create table student(
	studentid int,
    name varchar(100),
    courseid int
);

insert into stduent(studentid , name , courseid)
values
	(1 , 'rahul' , 101),
    (2 , 'Neha' , 102),
    (3 , 'aman' , 103);

create table course(
	courseid int,
    coursename varchar(100)
);

insert into course(courseid , coursename)
values
	(101 , 'python'),
    (102 , 'java');
    
SELECT Student.Name, Course.CourseName FROM Student INNER JOIN Course ON Student.CourseID = Course.CourseID;

SELECT Student.Name, Course.CourseName FROM Student INNER JOIN Course ON Student.CourseID = Course.CourseID WHERE Course.CourseName = 'Python';

CREATE VIEW PythonStudents AS
SELECT Student.Name, Course.CourseName
FROM Student
INNER JOIN Course
ON Student.CourseID = Course.CourseID
WHERE Course.CourseName = 'Python';
SELECT * FROM PythonStudents;  