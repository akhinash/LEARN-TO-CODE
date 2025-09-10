create database student;
CREATE TABLE stud( s_id VARCHAR(50) NOT NULL PRIMARY KEY, name VARCHAR(20) not NULL,age int NOT NULL, place varchar(20) not null);
INSERT INTO stud values ('s3','shareef',13,'palakkad');
SELECT*from stud;
INSERT INTO stud VALUES('s4','praveen',32,'thrissur'),('s5','john',20,'trivandrum'),('s6','akhil',20,'kochi'),('s7','aneesh',14,'kottayam');
SELECT*FROM stud;


SELECT*from stud where age>20;
SELECT*from stud where place='trivandrum';
SELECT*FROM stud where place='thrissur' AND age=32;