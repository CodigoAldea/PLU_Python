'''Question 10
Consider the following tables.
Student
| StudentID | Name | CourseID |
| --------- | ----- | -------- |
| 1 | Rahul | 101 |
| 2 | Neha | 102 |
| 3 | Aman | 101 |
Course
| CourseID | CourseName |
| -------- | ---------- |
| 101 | Python |
| 102 | Java |
Write SQL queries to:
1. Display Student Name and Course Name using an INNER JOIN.
2. Display only students enrolled in the Python course using the WHERE
clause.
3. Create a view named 'PythonStudents' for students enrolled in the Python
course.'''

-- here we are creating table student
CREATE TABLE Student(
    StudentID INT,
    Name VARCHAR(50),
    CourseID INT
);
-- here inserting data in student table
INSERT INTO Student VALUES
(1,'Rahul',101),
(2,'Neha',102),
(3,'Aman',101);

CREATE TABLE Course (
    CourseID INT,
    CourseName VARCHAR(50)
);

INSERT INTO Course VALUES
(101,'Python'),
(102,'Java');

-- here we joing the table using inner join studnet and course tbale
SELECT
Student.Name,
Course.CourseName
FROM Student
INNER JOIN Course
ON Student.CourseID=Course.CourseID;

-- here we using inner joing course and for python course slected student only python course
SELECT
Student.Name,
Course.CourseName
FROM Student
INNER JOIN Course
ON Student.CourseID=Course.CourseID
WHERE Course.CourseName='Python';
-- here creating view from pythonstudent student enroll this
CREATE VIEW PythonStudents AS
SELECT
-- here we are joining the table inner joing student coursse nd details 
Student.Name,
Course.CourseName
FROM Student
INNER JOIN Course
ON Student.CourseID=Course.CourseID
WHERE Course.CourseName='Python';

-- after join we display the student course slect details
SELECT * FROM PythonStudents;