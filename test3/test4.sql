
CREATE database test1; # created a database named test1
USE test1;

# ques 1
 # TASK 2: Make "EmployeeID" the primary key
ALTER TABLE Employee
ADD PRIMARY KEY (EmployeeID);

# task 1: created the table
CREATE TABLE Employee (
    EmployeeID INT,
    EmployeeName VARCHAR(100),
    Department VARCHAR(50),
    Salary INT,
    JoiningDate DATE,
    PRIMARY KEY (EmployeeID)
);



# que2 

CREATE TABLE Student (          
    StudentID INT PRIMARY KEY,
    Name VARCHAR(50),
    Course VARCHAR(50),
    Marks INT
);

INSERT INTO Student VALUES
(101, 'Rahul', 'Python', 80),
(102, 'Priya', 'Java', 75),
(103, 'Aman', 'Python', 90),
(104, 'Neha', 'SQL', 70);

#TASk 1: Display all student records.
SELECT * FROM Student;

#TASK 2: Display only Name and Marks
SELECT Name, Marks FROM Student;

#TASK 3: Display only Course column
SELECT Course FROM Student;

# que3

CREATE TABLE Product (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    Category VARCHAR(50),
    Price INT
);

INSERT INTO Product VALUES
(1, 'Mouse', 'Electronics', 800),
(2, 'Laptop', 'Electronics', 65000),
(3, 'Chair', 'Furniture', 4500),
(4, 'Keyboard', 'Electronics', 1200);

# TASK1: Display product costing more than 1000
SELECT * FROM Product WHERE Price > 1000;

# TASK 2: Display all electronic products
SELECT * FROM Product WHERE Category = 'Electronics';

#TASK3: Display all the laptop records
SELECT * FROM Product WHERE ProductName = 'Laptop';


# que4

CREATE TABLE Customer (       #TASK1: Create a Table
    CustomerID INT PRIMARY KEY,    #TASK2: Make CustomerID the PrimaryKey
    CustomerName VARCHAR(100),
    City VARCHAR(50),
    Mobile VARCHAR(15)
);

#TASK3: Why Primary keys are important
 # Primary key is a column which uniquely identifies each row
 # Its ensure Uniqueness as two same row cant have CustomerID, because of this Duplicating of data is avoided
 # It does not allow NULL values primary key column cannot be empty
 # Helps in creating Relationship, other tables can called using foriengh key throgh reference
 # Ensures data integrity is maintain

# que5

CREATE TABLE Employee1 (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(50),
    DepartmentID INT
);

CREATE TABLE Department (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(50)
);

INSERT INTO Employee1 VALUES
(1, 'Rahul', 101),
(2, 'Priya', 102),
(3, 'Aman', 101);

INSERT INTO Department VALUES
(101, 'IT'),
(102, 'HR');

# Write SQL query to display EmployeeName, Department Name using INNERJOIN
SELECT Employee1.Name, Department.DepartmentName
FROM Employee1
INNER JOIN Department
ON Employee1.DepartmentID = Department.DepartmentID;


# que 6

CREATE TABLE Course (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(50)
);

CREATE TABLE Student6 (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(50),
    CourseID INT
);

INSERT INTO Course VALUES
(201, 'Python'),
(202, 'SQL');

INSERT INTO Student6 VALUES
(1, 'Rahul', 201),
(2, 'Neha', 202),
(3, 'Aman', NULL);

#TASK: Write SQL Query to display all students along with  their course names using LEFT JOINN
SELECT Student6.Name, Course.CourseName
FROM Student6
LEFT JOIN Course
ON Student6.CourseID = Course.CourseID;

# que7

CREATE TABLE Employee7 (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(50),
    Department VARCHAR(50),
    Salary INT
);

INSERT INTO Employee7 VALUES
(1, 'Rahul', 'IT', 65000),
(2, 'Priya', 'HR', 45000),
(3, 'Aman', 'IT', 70000);

#TASK Create a view Named (HighSalaryEmployees)
CREATE VIEW HighSalaryEmployees AS
SELECT * FROM Employee7
WHERE Salary > 60000;

#TASK: Display employess earning more than 60k
SELECT * FROM HighSalaryEmployees;

# que 8

CREATE TABLE Orders (
    OrderID INT,
    CustomerName VARCHAR(100),
    OrderDate DATE,
    Amount INT
);

#TASK1: create a index on OrderID
CREATE INDEX idx_orderid ON Orders(OrderID);

#TASK2: Explain benefit of creating an Index
# Hels in Fast searching, index helps the database find data quickly
# Its Saves time as it reduces the time needed to retrieve records
# Improves performance so queries can run faster when an index is used
# Better efficiency because of this database works more efficiently with large amounts of data


# que9

CREATE TABLE Book (
    BookID INT PRIMARY KEY,
    BookName VARCHAR(100),
    Author VARCHAR(50),
    Price INT
);

INSERT INTO Book VALUES
(1, 'Python Basics', 'John', 500),
(2, 'Learning SQL', 'David', 700);

# TASK: Write stored procedure named 'GetBooks' that displays all records from the Book table
DELIMITER //

CREATE PROCEDURE GetBooks()
BEGIN
    SELECT * FROM Book;
END //

DELIMITER ;


CALL GetBooks();


# qus 10

CREATE TABLE Course10 (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(50)
);

CREATE TABLE Student10 (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(50),
    CourseID INT
);

INSERT INTO Course10 VALUES
(101, 'Python'),
(102, 'Java');

INSERT INTO Student10 VALUES
(1, 'Rahul', 101),
(2, 'Neha', 102),
(3, 'Aman', 101);


#Task1: Display Student Name and Course Name using an Inner Join 
SELECT Student10.Name, Course10.CourseName
FROM Student10
INNER JOIN Course10
ON Student10.CourseID = Course10.CourseID;

#Task2: Display only student enrolled in the Python course using the WHERE
SELECT Student10.Name, Course10.CourseName
FROM Student10
INNER JOIN Course10
ON Student10.CourseID = Course10.CourseID
WHERE Course10.CourseName = 'Python';

#Task3: Create View named 'PythonStudents' for students enrolled in PY course
CREATE VIEW PythonStudents AS
SELECT Student10.Name, Course10.CourseName
FROM Student10
INNER JOIN Course10
ON Student10.CourseID = Course10.CourseID
WHERE Course10.CourseName = 'Python';

SELECT * FROM PythonStudents;

