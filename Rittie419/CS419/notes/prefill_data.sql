SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `appt`;

-- Create a table to hold the appts
CREATE TABLE appt (
`id` int NOT NULL AUTO_INCREMENT,
`advisor_name` varchar(100),
`student_name` varchar(100),
`advisor_email` varchar(100),
`student_email` varchar(100),
`appointment_date` date,
`appointment_start_time` time,
`appointment_end_time` time,
`date_created` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (`id`)
) ENGINE=InnoDB;

-- Prefill Data
INSERT appt (advisor_name, student_name,
advisor_email, student_email, appointment_date, appointment_start_time,
appointment_end_time)
VALUES ("Jeff Rix", "Rittie Chuaprasert",
"rixj@onid.oregonstate.edu", "chuaprar@onid.oregonstate.edu",
"2015-02-09", "11:30:00", "12:00:00");

-- View initial Data
SELECT * FROM appt;

SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `appt`;

-- Create a table to hold the appts
CREATE TABLE appt (
`id` int NOT NULL AUTO_INCREMENT,
`advisor_name` varchar(100),
`student_name` varchar(100),--dkfjdkjgjg;;;;
`advisor_email` varchar(100),
`student_email` varchar(100),#ignore this;;;;
`appointment_date` date,
`appointment_start_time` time,
`appointment_end_time` time,
`date_created` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (`id`)
) ENGINE=InnoDB;

-- Prefill Data
INSERT appt (advisor_name, student_name,
advisor_email, student_email, appointment_date, appointment_start_time,
appointment_end_time)
VALUES ("Jeff Rix", "Rittie Chuaprasert",
"rixj@onid.oregonstate.edu", "chuaprar@onid.oregonstate.edu",
"2015-02-09", "11:30:00", "12:00:00");

-- View initial Data
SELECT * /* djkgjajgjfdgkjfadjgjhj */ F/*hello /*
dkfkdlkgkgkhhk
world*/ROM appt;/*
*/


INSERT appt 
(advisor_name, 
student_name,
advisor_email, 
student_email, 
appointment_date, 
appointment_start_time,
appointment_end_time) 
VALUES 
("Jeff Rix", 
"Rittie Chuaprasert",
"rixj@onid.oregonstate.edu", 
"chuaprar@onid.oregonstate.edu",
"2015-02-09", 
"11:30:00", 
"12:00:00");


mysql419 >>INSERT appt 
(advisor_name, 
student_name,
advisor_email, 
student_email, 
appointment_date, 
appointment_start_time,
appointment_end_time) 
VALUES 
("Jeff Rix", 
"Rittie Chuaprasert",
"rixj@onid.oregonstate.edu", 
"chuaprar@onid.oregonstate.edu",
"2015-02-09", 
"11:30:00", 
"12:00:00");

>>
>>
>>
>>
>>
>>

(query >> 'INSERT appt (advisor_name, student_name,advisor_email, student_email, appointment_date, appointment_start_time,appointment_end_time) VALUES ("Jeff Rix", "Rittie Chuaprasert","rixj@onid.oregonstate.edu", "chuaprar@onid.oregonstate.edu","2015-02-09", "11:30:00", "12:00:00");SELECT * FROM appt;')

>>SELECT * FROM appt;

+----+--------------+--------------------+---------------------------+-------------------------------+------------------+------------------------+----------------------+--------------+
| id | advisor_name | student_name       | advisor_email             | student_email                 | appointment_date | appointment_start_time | appointment_end_time | date_created |
+----+--------------+--------------------+---------------------------+-------------------------------+------------------+------------------------+----------------------+--------------+
|  1 | Jeff Rix     | Rittie Chuaprasert | rixj@onid.oregonstate.edu | chuaprar@onid.oregonstate.edu | 2015-02-09       | 11:30:00               | 12:00:00             | NULL         |
+----+--------------+--------------------+---------------------------+-------------------------------+------------------+------------------------+----------------------+--------------+







/* ======================================== */

-- before adding demo table
show databases;
show tables;

/* ======================================== */

-- add demo table
SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS 'demo_table';

CREATE TABLE 'demo_table'(
'id' INT(11) AUTO_INCREMENT,
'name' VARCHAR(255),
PRIMARY KEY ('id')
) ENGINE=InnoDB;

/* ======================================== */

-- after adding demo table
show tables;
SHOW CREATE TABLE 'demo_table';

/* ======================================== */

SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `appt`;

-- Create a table to hold the appts
CREATE TABLE appt (
`id` int NOT NULL AUTO_INCREMENT,
`advisor_name` varchar(100),
`student_name` varchar(100),
`advisor_email` varchar(100),
`student_email` varchar(100),
`appointment_date` date,
`appointment_start_time` time,
`appointment_end_time` time,
`date_created` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (`id`)
) ENGINE=InnoDB;

-- Prefill Data
INSERT appt (advisor_name, student_name,
advisor_email, student_email, appointment_date, appointment_start_time,
appointment_end_time)
VALUES ("Jeff Rix", "Rittie Chuaprasert",
"rixj@onid.oregonstate.edu", "chuaprar@onid.oregonstate.edu",
"2015-02-09", "11:30:00", "12:00:00");

-- View initial Data
SELECT * FROM appt;

/* ======================================== */


SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `temp`;

-- Create a table to hold the appts
CREATE TABLE temp (
`id` int NOT NULL AUTO_INCREMENT,
`advisor_name` varchar(100),
`student_name` varchar(100),
`advisor_email` varchar(100),
`student_email` varchar(100),
`appointment_date` date,
`appointment_start_time` time,
`appointment_end_time` time,
`date_created` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (`id`)
) ENGINE=InnoDB;

-- Prefill Data
INSERT temp (advisor_name, student_name,
advisor_email, student_email, appointment_date, appointment_start_time,
appointment_end_time)
VALUES ("Jeff Rix", "Rittie Chuaprasert",
"rixj@onid.oregonstate.edu", "chuaprar@onid.oregonstate.edu",
"2015-02-09", "11:30:00", "12:00:00");

-- View initial Data
SELECT * FROM temp;

/* ======================================== */

