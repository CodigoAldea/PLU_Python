-- Question 9
-- Consider the following table.
-- Book
-- | BookID | BookName | Author | Price |
-- | ------ | ------------- | ------ | ----- |
-- | 1 | Python Basics | John | 500 |
-- | 2 | Learning SQL | David | 700 |
-- Write a stored procedure named 'GetBooks' that displays all records from the
-- Book table.

CREATE TABLE Book (
    BookID INT PRIMARY KEY,
    BookName VARCHAR(100),
    Author VARCHAR(100),
    Price INT
);


CREATE PROCEDURE GetBooks

BEGIN SELECT * FROM Book;
END;

call GetBooks;