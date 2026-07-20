'''Question 6
Consider the following tables.
Student
| StudentID | Name | CourseID |
| --------- | ----- | -------- |
| 1 | Rahul | 201 |
| 2 | Neha | 202 |
| 3 | Aman | NULL |
Course
| CourseID | CourseName |
| -------- | ---------- |
| 201 | Python |
| 202 | SQL |
Write an SQL query to display all students along with their course names
using a LEFT JOIN.'''

-- here we are creating data table student
CREATE TABLE Student (
    StudentID INT,
    Name VARCHAR(50),
    CourseID INT
);

-- Inserting  data in data table 
INSERT INTO Student VALUES
(1,'Rahul',201),
(2,'Neha',202),
(3,'Aman',NULL);

-- here creating course  data table
CREATE TABLE Course (
    CourseID INT,
    CourseName VARCHAR(50)
);

-- inserting data in course table
INSERT INTO Course VALUES
(201,'Python'),
(202,'SQL');

-- here left join using we join student and course
SELECT
Student.Name,
Course.CourseName
FROM Student
LEFT JOIN Course
ON Student.CourseID=Course.CourseID;