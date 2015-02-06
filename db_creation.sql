SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `appointment`;

-- Create a table to hold the appointments
CREATE TABLE  appointment (
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


--Prefill Data
INSERT INTO appointment (advisor_name, student_name,
advisor_email, student_email, appointment_date, appointment_start_time,
appointment_end_time)
VALUES ("Jeff Rix", "Rittie Chuaprasert",
"rixj@onid.oregonstate.edu", "chuaprar@onid.oregonstate.edu",
"2015-02-09", "11:30:00", "12:00:00");
