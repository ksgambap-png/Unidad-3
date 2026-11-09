CREATE DATABASE mi_db_1;
USE mi_db_1;

CREATE TABLE empleados (
	Employee_ID VARCHAR (20) PRIMARY KEY,
    Full_name VARCHAR (120),
    Job_Title VARCHAR (100),
    Department VARCHAR (120),
    Business_Unit VARCHAR (130),
    Gender VARCHAR(50),
    Ethnicity VARCHAR (70),
    Age INT,
    Annual_Salary DECIMAL (12,2),
    Bonus DECIMAL (10,2)
)