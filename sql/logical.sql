use student;
SELECT*from stud
where age=32 or place='trivandrum';
SELECT*from stud
where age=32 and place='thrissur'; 
SELECT*from stud
where place!= 'kozhikode';

-- between

SELECT*from stud
where age BETWEEN 20 and 33;

SELECT*from stud
where age not BETWEEN 20 and 33;

-- in

SELECT * FROM stud
where place in('kozhikode','thrissur');

SELECT * FROM stud
where place not in('kozhikode','thrissur');


-- exist
SELECT * FROM stud
where EXISTS(select age from stud where age<20);




CREATE TABLE emp1 (
id int PRIMARY KEY, name VARCHAR(20), salary int, department VARCHAR(20),dob date, progress VARCHAR(10), emp_code varchar(20));
insert into emp1 VALUES
(101,'jack',2000,'HR','1997-05-19','30%','jack-101' ),
(102,'jack',90000,'HR','2000-09-07','75%', 'jack-102'),
(103,'mack',6000,'Developer','1997-03-10','10%', 'mack-103'),
(104,'peter',4000,'tester','1998-11-16','15%', 'peter-104'),
(105,'tom',3000,'HR','1998-11-03','11%', 'tom-105');

SELECT*from emp1;

SELECT*from emp1
WHERE name LIKE '%o%';

SELECT*from emp1
WHERE name LIKE 't%';

SELECT*from emp1
WHERE name LIKE 'k%';

SELECT*FROM emp1
WHERE name like '%\_%';

SELECT*from emp1
WHERE name LIKE 't_m%';


SELECT*FROM emp1
WHERE name like '%\%%';

Select id,name,dob from emp1
where dob not like '%_3_%';



CREATE TABLE Emp3 (
    ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Gender CHAR(1),
    Designation VARCHAR(50),
    Salary INT,
    City VARCHAR(50)
);

INSERT INTO Emp3 (ID, Name, Gender, Designation, Salary, City)
VALUES 
(1, 'Anish', 'M', 'SSE', 50000, 'kochi'),
(2, 'Sijah', 'M', 'SSE', 60000, 'kochi'),
(3, 'Arun', 'M', 'SE', 40000, 'TVM'),
(4, 'Sreeni', 'F', 'SE', 45000, 'TVM'),
(5, 'Anju', 'F', 'S', 30000, 'Kollam'),
(6, 'Reshma', 'F', 'SE', 320000, 'kochi');

SELECT * FROM Emp3;

SELECT city,sum(salary) as tsal
from emp3
GROUP BY city;

SELECT gender,count(*) as emp_count
from emp3
group by gender;

SELECT city,designation,sum(salary) from emp3
group by city,designation
order by city;

-- group by with where clause

SELECT city,gender,designation,sum(salary) from emp3
where gender='m'
group by city,designation
order by city;

SELECT city,gender,designation,sum(salary) from emp3

group by city,designation,gender
having gender='m'
order by city;


SELECT city,sum(salary) as tsal1
from emp3
group by city
having sum(salary)>50000;

create table stud1( id int unique,name varchar(255),age int,grade VARCHAR(10));
insert into stud1 VALUES(001,'akhinash',24,'A'),
(002,'achu',24,'A'),
(003,'srk',22,'B'),
(004,'vijay',23,'F'),
(005,'yash',26,'A');

SELECT grade,count(*) from stud1
GROUP BY grade;

SELECT grade,avg(age) as 'avgage' from stud1
GROUP BY grade;

SELECT grade,avg(age) as 'avgage' from stud1
GROUP BY grade
HAVING avg(age)>12;

SELECT grade,count(*) as'avgage' from stud1
GROUP BY grade
having count(*)>2;
