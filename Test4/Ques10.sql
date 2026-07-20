SELECT Student.Name, Course.CourseName
FROM Student
INNER JOIN Course
ON Student.CourseID = Course.CourseID;


SELECT Student.Name, Course.CourseName
FROM Student
INNER JOIN Course
ON Student.CourseID = Course.CourseID
WHERE Course.CourseName = 'Python';


CREATE VIEW PythonStudents AS
SELECT Student.Name, Course.CourseName
FROM Student
INNER JOIN Course
ON Student.CourseID = Course.CourseID
WHERE Course.CourseName = 'Python';