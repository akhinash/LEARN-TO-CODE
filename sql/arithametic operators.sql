CREATE TABLE employee1 (
    EmployeeID INT PRIMARY KEY,
    Salary INT,
    Bonus INT
);

INSERT INTO employee1 (EmployeeID, Salary, Bonus) VALUES
(1, 50000, 5000),
(2, 60000, 7000),
(3, 45000, 4000);

SELECT * FROM employee1;

SELECT EmployeeID, Salary+Bonus as Totalcompensation
from employee1;

SELECT EmployeeID, Salary-Bonus as Remain
FROM employee1;

SELECT EmployeeID, Bonus*2 AS DOUBLEBONUS
FROM employee1;

SELECT EmployeeID, (Bonus*100)/Salary AS bpercentage
FROM employee1;

SELECT EmployeeID, Bonus%3000 AS Remainder
FROM employee1;

