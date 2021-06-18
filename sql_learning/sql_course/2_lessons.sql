-- Insert
-- Select 

DROP TABLE IF EXISTS "Employee" CASCADE;

CREATE TABLE IF NOT EXISTS employee (
	employee_id SERIAL PRIMARY KEY,
	user_name VARCHAR(128) NOT NULL,
	password VARCHAR(128) NOT NULL,
	email VARCHAR(128),
	is_new BOOLEAN,
	born_year INTEGER NOT NULL,
	start_work TIMESTAMP NOT NULL,
	salary INTEGER NOT NULL
);

-- Exercise: Add 5 items to TABLE employee

INSERT INTO employee(user_name, password, email, is_new, born_year, start_work, salary) 
VALUES ('Norbert','Heslo','norbert.bago@gmail.com',TRUE, 1991, '2021-01-16 19:10:25-07',1500);

INSERT INTO employee(user_name, password, email, is_new, born_year, start_work, salary) 
VALUES ('Paula','Heslo','paula.bagova@gmail.com',FALSE, 1989, '2021-01-16 19:10:25-07',1000);

INSERT INTO employee(user_name, password, email, is_new, born_year, start_work, salary) 
VALUES ('Laura','Heslo','laura.bagova@gmail.com',FALSE, 1989, '2021-01-16 19:10:25-07',1800);

INSERT INTO employee(user_name, password, email, is_new, born_year, start_work, salary) 
VALUES ('Neo','Heslo','neo.bago@gmail.com',TRUE 2025, '2021-01-16 19:10:25-07',2500);

INSERT INTO employee(user_name, password, email, is_new, born_year, start_work, salary) 
VALUES ('Sofia','Heslo','sofia.bagova@gmail.com',FALSE, 1989, '2021-01-16 19:10:25-07',2500);






