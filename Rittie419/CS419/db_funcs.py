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

table = "'temp'"

# Returns all the data in the database
# @return contents of database in nested list format:  
#	[[row1field1,row1field2,...], [row2field1,row2field2,...], ...]
def view_appt():
	query = 'SELECT * FROM %s' % (table)
	table_borders = False
	appts = execute(query, table_borders)
	appts = appts.split('\n')
	for r in range(len(appts)):
		appts[r] = appts[r].split('\t')
		if (len(appts[r])==1):
			appts.pop(r)

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
def add_appt(adv, stud, adv_email, stud_email, date, start, end):

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
def drop_appt_by_id(unique_id):

	query = '''
		DELETE FROM %s WHERE
			('id'=%s);
	''' % (table, str(unique_id))
	print query
	print execute(query)	

	return         
        
        
# Drops an appointment from the appointmnt database unless it's a conflict
# @param date	appointment date
# @param start	appointment start time
# @return	unique ID associated with appointment
def drop_appt(date, start):
	unique_id = get_unique_id(date, start)

	query = '''
		DELETE FROM %s WHERE
			('appointment_date'="%s" AND 'appointment_start_time'="%s");
	''' % (table, date, start)
	print query
	print execute(query)
	print execute('SELECT * FROM %s;' % (table))

	return unique_id

# returns a unique id to be applied to a calendar appointment
# by convention, the FORMAT=
# 	'{student_email}::{appointment_date}::{appointment_start_time}'
# @return unique in FORMAT above
def get_unique_id(date, start):
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
def get_student(date, start):
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
def is_repeat(date, start, end):
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

