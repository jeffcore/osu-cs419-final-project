from sql_cmd import execute

table = "'temp'"

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

