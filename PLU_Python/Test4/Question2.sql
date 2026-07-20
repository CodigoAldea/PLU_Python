'''Question 2
Consider the following table.
Student
| StudentID | Name | Course | Marks |
| --------- | ----- | ------ | ----- |
| 101 | Rahul | Python | 80 |
| 102 | Priya | Java | 75 |
| 103 | Aman | Python | 90 |
| 104 | Neha | SQL | 70 |
Write SQL queries to:
1. Display all student records.
2. Display only Name and Marks.
3. Display only the Course column.'''


-- here we creating table in database one where we create student table 
CREATE TABLE Student (
    StudentID INT,
    Name VARCHAR(50),
    Course VARCHAR(50),
    Marks INT
);

-- here we insert student datat in table 
INSERT INTO Student VALUES
(101,'Rahul','Python',80),
(102,'Priya','Java',75),
(103,'Aman','Python',90),
(104,'Neha','SQL',70);

--  here we diplaying  marks recorded course
-- display all student records 
SELECT * FROM Student;
-- display student only name and marks 
SELECT Name, Marks
FROM Student;
-- display only course columsn
SELECT Course
FROM Student;