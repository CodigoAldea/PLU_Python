'''Question 9
Consider the following table.
Book
| BookID | BookName | Author | Price |
| ------ | ------------- | ------ | ----- |
| 1 | Python Basics | John | 500 |
| 2 | Learning SQL | David | 700 |
Write a stored procedure named 'GetBooks' that displays all records from the
Book table.'''

-- here we are creating datatable book
CREATE TABLE Book (
    BookID INT,
    BookName VARCHAR(100),
    Author VARCHAR(50),
    Price INT
);

-- here we are inserting data in book table
INSERT INTO Book VALUES
(1,'Python Basics','John',500),
(2,'Learning SQL','David',700);

-- here creating storage procedure
CREATE PROCEDURE GetBooks()
BEGIN
SELECT * FROM Book
END;

DELIMITER;
-- here we calling the function
CALL GetBooks();