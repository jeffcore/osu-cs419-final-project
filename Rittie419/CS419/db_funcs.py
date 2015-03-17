'''
This module contains the database commands needed to execute CS419 Project
Simplifed Advising Scheduling for our implementation.

# Usage:
import db_funcs
db_funcs.{function_call}	# exampl: db_funcs.add_appt(arguments...)

# OR import functions directly
from db_funcs import view_appt, add_appt, drop_appt, ...
'''

from sql_cmd import execute

DEFAULT_TABLE = 'appointment'

def get_table_name():
	return DEFAULT_TABLE

# Returns all the data in the database
def view_appt(table = DEFAULT_TABLE):
	query = 'SELECT * FROM %s' % (table)
	appts = execute(query)
	return appts

# Adds an appointment to the appointmnt database unless it's a conflict
# @param adv	advisor name
# @param stud	student name
# @param adv_email	advisor email
# @param stud_email	student email
# @param date	appointment date
# @param start	appointment start time
# @param end	appointment end time
# @return	unique ID associated with appointment
def add_appt(adv, stud, adv_email, stud_email, date, start, end, table = DEFAULT_TABLE):

	if is_repeat(date, start, end):
		print "Meeting conflict - new appointment not added."
		return 0

	else:

		query = '''
			INSERT INTO %s (
				advisor_name, 
				student_name, 
				advisor_email, 
				student_email,
				appointment_date,
				appointment_start_time,
				appointment_end_time)
			''' % table
		query += '''
			VALUES (
				"%s", 
				"%s", 
				"%s", 
				"%s", 
				"%s", 
				"%s", 
				"%s");
			''' % (adv, stud, adv_email, stud_email, date, start, end);

		print query
		print execute(query)
		print execute('SELECT * FROM %s;' % (table))
		unique_id = get_unique_id(date, start)

		return unique_id


# Drops an appointment from the appointmnt database 
# @param date	appointment date
# @param start	appointment start time
# @return	unique ID associated with appointment
def drop_appt_by_id(unique_id, table = DEFAULT_TABLE):

	query = '''
		DELETE FROM %s WHERE
			('id'=%s);
	''' % (table, str(unique_id))
	#print query
	execute(query)	

	return         
        
        
# Drops an appointment from the appointmnt database unless it's a conflict
# @param date	appointment date
# @param start	appointment start time
# @return	unique ID associated with appointment
def drop_appt(date, start, table = DEFAULT_TABLE):
	unique_id = get_unique_id(date, start)

	query = '''
		DELETE FROM %s WHERE
			('appointment_date'="%s" AND 'appointment_start_time'="%s");
	''' % (table, date, start)
	query
	execute(query)
	#print execute('SELECT * FROM %s;' % (table))

	return unique_id

# returns a unique id to be applied to a calendar appointment
# by convention, the FORMAT=
# 	'{student_email}::{appointment_date}::{appointment_start_time}'
# @return unique in FORMAT above
def get_unique_id(date, start, table = DEFAULT_TABLE):
	query = '''
		SELECT 'student_email' FROM %s WHERE
			('appointment_date'="%s" AND 'appointment_start_time'="%s");
	''' % (table, date, start)

	email = execute(query, False).strip()
	unique_id = email + '::' + date + '::' + start

	return unique_id

# Returns student name associated with an appointment
# @param date	appointment date
# @param start	appointment start time
# @return	student name
def get_student(date, start, table = DEFAULT_TABLE):
	query = '''
		SELECT 'student_name' FROM %s WHERE
			('appointment_date'="%s" AND 'appointment_start_time'="%s");
	''' % (table, date, start)

	student = execute(query, False).strip()

	return student

# Determines whether a new appointment conflicts with existing appointment
# @param date	appointment date
# @param start	appointment start time
# @param end	appointment end time
# @return	True if conflict exists, False otherwise
def is_repeat(date, start, end, table = DEFAULT_TABLE):
	conflict_found = False
	query = '''
		SELECT 'id' FROM %s WHERE 
			'appointment_date'="%s" AND (
			('appointment_start_time'="%s" OR 'appointment_end_time'="%s") OR
			('appointment_start_time'>"%s" AND 'appointment_start_time'<"%s") OR
			('appointment_end_time'>"%s" AND 'appointment_end_time'<"%s"));
		''' % (table, date, start, end, start, end, start, end)

#	print query
#	print execute(query, False)
	if len( execute(query, False) ) > 0:
		conflict_found = True

	return conflict_found

# Initializes a new blank table in cs496-g8 database
# @param table	name of new blank table in cs496-g8 database
def new_table(table):

	print 'Tables BEFORE:\n'
	print execute('show tables;')
	print '------------------------------------'
	query = '''
		SET FOREIGN_KEY_CHECKS=0;
		DROP TABLE IF EXISTS `%s`;

		-- Create a table to hold the appts
		CREATE TABLE `%s` (
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
		''' % (table, table)

	execute(query, False)
	print 'Tables AFTER:\n'
	print execute('show tables;')
	print execute('show create table %s;' % table, False)


# Drops a table from cs496-g8 database (FOR TESTING / VALIDATION ONLY)
# @param table	name of table to drop from cs496-g8 database
def drop_table(table):

	print 'Tables BEFORE:\n'
	print execute('show tables;')
	print '------------------------------------'
	query = '''
		SET FOREIGN_KEY_CHECKS=0;
		DROP TABLE IF EXISTS `%s`;
		''' % (table)

	execute(query, False)
	print 'Tables AFTER:\n'
	print execute('show tables;')


