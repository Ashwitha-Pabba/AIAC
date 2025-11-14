-- Drop tables if they exist (resets everything for each run)
DROP TABLE IF EXISTS Attendance;
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Courses;

-- Create Students Table
CREATE TABLE IF NOT EXISTS Students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(32),
    last_name VARCHAR(32),
    email VARCHAR(64)
);

-- Create Courses Table
CREATE TABLE IF NOT EXISTS Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(64),
    description TEXT
);

-- Create Attendance Table
CREATE TABLE IF NOT EXISTS Attendance (
    attendance_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    attendance_date DATE,
    status ENUM('Present', 'Absent'),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Insert Sample Data into Students Table
INSERT INTO Students VALUES (1, 'Alice', 'Sharma', 'alice.sharma@email.com');
INSERT INTO Students VALUES (2, 'Rohit', 'Singh', 'rohit.singh@email.com');
INSERT INTO Students VALUES (3, 'Meena', 'Kumar', 'meena.kumar@email.com');

-- Insert Sample Data into Courses Table
INSERT INTO Courses VALUES (1, 'Mathematics', 'Basic math course');
INSERT INTO Courses VALUES (2, 'Physics', 'Introductory physics');

-- Insert Sample Data into Attendance Table
INSERT INTO Attendance VALUES (1, 1, 1, '2025-11-01', 'Present');
INSERT INTO Attendance VALUES (2, 1, 1, '2025-11-02', 'Absent');
INSERT INTO Attendance VALUES (3, 2, 2, '2025-11-01', 'Present');
INSERT INTO Attendance VALUES (4, 3, 1, '2025-11-01', 'Absent');
INSERT INTO Attendance VALUES (5, 3, 1, '2025-11-02', 'Absent');

-- Print all Student records
SELECT * FROM Students;
SELECT * FROM Courses;
SELECT * FROM Attendance;

-- Query to Find Students with Attendance Below 75%
SELECT
    Students.student_id,
    Students.first_name,
    Students.last_name,
    Courses.course_id,
    Courses.course_name,
    (SUM(CASE WHEN Attendance.status = 'Present' THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS attendance_percentage
FROM
    Attendance
JOIN
    Students ON Attendance.student_id = Students.student_id
JOIN
    Courses ON Attendance.course_id = Courses.course_id
GROUP BY
    Students.student_id, Courses.course_id
HAVING
    (SUM(CASE WHEN Attendance.status = 'Present' THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) < 75;
