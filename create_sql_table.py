""" Write a SQL statement to create a table employees including columns employee_id, first_name, last_name, email,
phone_number hire_date, job_id, salary, commission, manager_id and department_id and 
make sure that, the employee_id column does not contain any duplicate value at the time of insertion, and the foreign key column department_id, 
reference by the column department_id of departments table,
can contain only those values which are exists in the departments table and another foreign key column job_id, 
referenced by the column job_id of jobs table, can contain only those values which are exists in the jobs table."""

CREATE TABLE IF NOT EXISTS employees ( 
EMPLOYEE_ID decimal(6,0) NOT NULL PRIMARY KEY, 
FIRST_NAME varchar(20) DEFAULT NULL, 
LAST_NAME varchar(25) NOT NULL, 
EMAIL varchar(25) NOT NULL, 
PHONE_NUMBER varchar(20) DEFAULT NULL, 
HIRE_DATE date NOT NULL, 
JOB_ID varchar(10) NOT NULL, 
SALARY decimal(8,2) DEFAULT NULL, 
COMMISSION_PCT decimal(2,2) DEFAULT NULL, 
MANAGER_ID decimal(6,0) DEFAULT NULL, 
DEPARTMENT_ID decimal(4,0) DEFAULT NULL, 
FOREIGN KEY(DEPARTMENT_ID) 
REFERENCES  departments(DEPARTMENT_ID),
FOREIGN KEY(JOB_ID) 
REFERENCES  jobs(JOB_ID)

dese employees
