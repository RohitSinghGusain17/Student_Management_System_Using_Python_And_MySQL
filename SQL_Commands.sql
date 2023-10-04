create table STUDENT(RollNo int NOT NULL UNIQUE,Name varchar(255),FatherName varchar(255),MotherName varchar(255),Address varchar(255),PhoneNo int,Email varchar(255));
create table EXAM(RollNo int NOT NULL UNIQUE,Name varchar(255),Class int,Section varchar(255),TotalMarks int,Percentage int,Grade varchar(255));
