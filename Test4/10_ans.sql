-- Question 10
-- Consider the following tables.
-- Student
-- | StudentID | Name | CourseID |
-- | --------- | ----- | -------- |
-- | 1 | Rahul | 101 |
-- | 2 | Neha | 102 |
-- | 3 | Aman | 101 |
-- Course
-- | CourseID | CourseName |
-- | -------- | ---------- |
-- | 101 | Python |
-- | 102 | Java |
-- Write SQL queries to:
-- 1. Display Student Name and Course Name using an INNER JOIN.
-- 2. Display only students enrolled in the Python course using the WHERE
-- clause.
-- 3. Create a view named 'PythonStudents' for students enrolled in the Python course.

CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(100),
    CourseID INT
);

INSERT INTO Student (StudentID, Name, CourseID) VALUES
(1, 'Rahul', 101),
(2, 'Neha', 102),
(3, 'Aman', 101);

CREATE TABLE Course (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100)
);

INSERT INTO Course (CourseID, CourseName) VALUES
(101, 'Python'),
(102, 'Java');

SELECT Student.Name, Course.CourseName
FROM Student
INNER JOIN Course ON Student.CourseID = Course.CourseID;

SELECT * FROM Student
WHERE CourseName = 'Python';



CREATE VIEW PythonStudents AS
SELECT CourseID, Name
FROM Student
WHERE CourseName = 'Python';