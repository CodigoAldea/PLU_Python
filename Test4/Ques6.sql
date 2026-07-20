SELECT Student.Name, Course.CourseName
FROM Student
LEFT JOIN Course
ON Student.CourseID = Course.CourseID;