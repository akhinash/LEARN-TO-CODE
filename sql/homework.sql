CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(100),
    Department VARCHAR(50),
    Salary INT
);

ALTER TABLE Employees ADD Email VARCHAR(100);
ALTER TABLE Employees MODIFY Salary DECIMAL(10,2);
SELECT * FROM Employees;

INSERT INTO Employees (EmployeeID, Name, Department, Salary, Email)
VALUES 
(1, 'john', 'Sales', 60000, 'john@gmail.com'),
(2, 'arjun', 'Marketing', 55000, 'ar@gmail.com'),
(3, 'lolan', 'IT', 70000, 'lol@gmail.com'),
(4, 'David', 'Sales', 48000, 'david@gmail.com'),
(5, 'sandy', 'HR', 52000, 'sand@gmail.com');

SELECT * FROM Employees WHERE Department = 'Sales';

SELECT Name, Salary FROM Employees WHERE Salary > 50000;


UPDATE Employees
SET Salary = Salary+(Salary*10)/100 WHERE Department='Marketing';

ALTER TABLE Employees add age int;
SELECT*from Employees;
INSERT into Employees (age) VALUES
(20),(30),(68),(57),(43);

use tech;

UPDATE Employees
SET Salary = Salary + (Salary * 10) / 100
WHERE Department = 'Marketing';


