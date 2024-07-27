create database python_db;

use python_db;


create table course(
		id INT AUTO_INCREMENT PRIMARY KEY,
        cname VARCHAR(50) NOT NULL,
        description VARCHAR(250),
        duration VARCHAR(50)
);


select * from course;