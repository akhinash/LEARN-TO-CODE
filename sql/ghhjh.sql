USE company;
CREATE TABLE contacts(  contact_id INT PRIMARY KEY,name VARCHAR(20),phone_number varchar(20) UNIQUE,
 email VARCHAR(50) unique);
 INSERT INTO contacts VALUES(1, 'aarav','9876543210','arav.kumar@example.com'),
 (2,'diya nair','854601256',null),(3,'ishaan rao','956696565',NULL);

SELECT*from contacts;

create table empl (
id int not null, nam varchar(50) null, dateofjoin date DEFAULT '2025-12-30');
INSERT into empl (id,nam)VALUES(3,'john doe');
select*from empl;




CREATE DATABASE University;
USE University;
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100)
);

CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(100),
    Age INT,
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

INSERT INTO Departments (DepartmentID, DepartmentName) VALUES
(1, 'Computer Science'),
(2, 'Mechanical Engineering'),
(3, 'Electrical Engineering');

select * FROM Departments;

INSERT INTO Students (StudentID, StudentName, Age, DepartmentID) VALUES
(1, 'akshara', 20, 1),
(2, 'prarthana', 22, 2),
(3, 'namitha', 21, 3);

select * FROM Students;

UPDATE Departments
SET DepartmentName = 'Mech'
WHERE DepartmentID = 2;

select * FROM Departments;


ALTER TABLE Students ADD Email VARCHAR(100);

select * FROM Students;
UPDATE Students SET Email = 'aksh@gmail.com' WHERE StudentID = 1;
UPDATE Students SET Email = 'prart@gmail.com' WHERE StudentID = 2;
UPDATE Students SET Email = 'nami@gmail.com' WHERE StudentID = 3;

select * FROM Students;

delete from Students 
where StudentId=2;

truncate TABLE Departments;




