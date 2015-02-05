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
	`date_created` date,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB;
