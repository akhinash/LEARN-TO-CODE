create DATABASE techoo;

use student;
create table studds like stud;
INSERT INTO studds SELECT*FROM stud;
SELECT*from studds;

CREATE DATABASE company;
USE company;
CREATE TABLE comp(company_id int NOT NULL PRIMARY KEY, company_name VARCHAR(20) not NULL, location VARCHAR(30) not NULL,product_type varchar(30) not null,yearly_revenue int not null, established_year int not null); 
INSERT INTO comp (company_id, company_name, location, product_type, yearly_revenue, established_year) VALUES
(1, 'Kerala Textiles Ltd', 'Kozhikode, Kerala', 'Cotton Fabrics', 5000000, 1998),
(2, 'Southern Looms', 'Ernakulam, Kerala', 'Silk Sarees', 7500000, 2005),
(3, 'Malabar Weaves', 'Thrissur, Kerala', 'Handwoven Fabrics', 3000000, 1985),
(4, 'Nila Textiles', 'Kannur, Kerala', 'Synthetic Fabrics', 4500000, 2010);
SELECT*FROM comp;

DELETE FROM comp where company_id =4;

SELECT * FROM comp ORDER BY company_id ASC
limit 2;
SELECT * FROM comp ORDER BY company_id DESC
limit 2;
SELECT * FROM comp ORDER BY rand()
limit 2;

SELECT company_name as name,location as place from comp;
SELECT*from comp;

SELECT *from comp as comps;