'''
The procfilter.py module is launched by .procmailrc from the linux
shell upon identifying an advisor system email (either an appointment 
add or drop).  The text of the email is passed in via stdin.

proc


'''

import sys
import email
from datetime import datetime
import get_email, db_funcs, add_calendar
from db_funcs import view_appt, add_appt, drop_appt
DEMARC_KEY = 'Name: REDACTED'

# ========================================================== #

def main():

	# store complete text of incoming email message
	email_parsed_by_row = sys.stdin.readlines()
	email_msg = ''.join(email_parsed_by_row)

	# determine whether email is an appointment drop
	is_drop = True if (
		email_msg.count('Advising Signup Cancel') == 1) else False

	# handle case of an appointment drop
	if (is_drop):
		handle_drop(email_msg)

	# handle case of an appointment add
	else:
		handle_add(email_msg)

# ========================================================== #
# -------------------------------------------------- #
'''
			INSERT INTO %s (
				advisor_name, 
				student_name, 
				advisor_email, 
				student_email,
				appointment_date,
				appointment_start_time,
				appointment_end_time)
			'''
def handle_add(msg):

	print msg
	print '\t\t------------------------------'

	# extract necessary data from email message
	db_adv = get_db_advisor(msg)
	db_stud = get_db_student(msg)
	db_adv_email = get_db_advisor_email(msg)
	db_stud_email = get_db_student_email(db_stud)
	db_date = get_db_date(msg)
	db_start = get_db_starttime(msg)
	db_end = get_db_endtime(msg)
	uid = '%s::%s::%s' % (db_stud_email, db_date, db_start)

	y = int(db_date[0:4])
	m = int(db_date[5:7])
	d = int(db_date[8:10])
	hour = int(db_start[0:2])
	mins = int(db_start[3:5])
#	print y, m, d
#	print hour, mins
	dt_start = datetime(y, m, d, hour, mins)

	hour = int(db_end[0:2])
	mins = int(db_end[3:5])
	dt_end = datetime(y, m, d, hour, mins)

	print dt_start.strftime("%A, %B %d, %Y  %I:%M%p")
	print dt_end.strftime("%A, %B %d, %Y  %I:%M%p")

	f = open('CS419/CS419mail/proc_add_output.txt', 'w')
	f.write(msg)
	f.close()

	#	(FOR TESTING) store email and database field data 
	print '\t\t------------------------------'
	print '%s\n%s\n%s\n%s\n%s\n%s\n%s' % (db_adv, db_stud,
		db_adv_email, db_stud_email, db_date, db_start, db_end)
	print '\t\t------------------------------'

	# update database with new appointment
	db_funcs.add_appt(db_adv, db_stud,
		db_adv_email, db_stud_email, db_date, db_start, db_end)

	# send Outlook calendar invite to advisor
	add_calendar.add_calendar(db_adv, db_stud,
		db_adv_email, dt_start, dt_end, uid)

	# send confirmation email to student


	return
# -------------------------------------------------- #
def get_db_advisor(msg):
	key1 = 'Advising Signup with'
	key2 = 'confirmed'
	advisor = findtext(msg, key1, key2)
	return advisor
# -------------------------------------------------- #
def get_db_student(msg):
	key1 = 'confirmed for'
	key2 = 'Advising Signup'
	student = findtext(msg, key1, key2)
	return student
# -------------------------------------------------- #
def get_db_advisor_email(msg):
	key1 = 'To: REDACTED@engr.orst.edu,'
	key2 = 'Cc:'
	emailaddr = findtext(msg, key1, key2)
	return emailaddr
# 	------------------------------------------------
def findtext(msg, key1, key2):
	tag1 = msg.find(key1) + len(key1)
	tag2 = msg[tag1:].find(key2) + tag1
	text = msg[tag1:tag2].strip()
	if ',' in text:
		tag3 = text.find(',')
		text = '%s, %s' % (text[:tag3], text[tag3+1:].strip())
	return text
# -------------------------------------------------- #
def get_db_student_email(student):
	argv = []
	argv.append(student)
	print argv
	emailaddr = get_email.main([student])
	print emailaddr
	return emailaddr
# -------------------------------------------------- #
def get_db_date(msg):
	date_sig = get_date_signature(msg)
	db_date = return_date(date_sig)
	return db_date

def get_date_signature(msg):
	tag = msg.find(DEMARC_KEY)
	msg = msg[tag:]			# advance past header info
	tag = msg.find('Date:')
	msg = msg[tag+5:]		# advance to date signature
	tag = msg.find('\n')
	sig = msg[:tag].strip()	# final date signature
	return sig

def return_date(sig):
	parsed = sig.split(', ')
#	print parsed

	year = parsed[2]
	month_day = parsed[1].split(' ')
	raw_month = month_day[0]
	raw_day = month_day[1]
#	print raw_month, raw_day, year

	month = get_month_num(raw_month)
	day = get_day_num(raw_day)
	date = '%s-%s-%s' % (year, month, day)
	print date

	return date

def get_month_num(m):

	lookup = {	'January':	'01',
				'February':	'02',
				'March': 	'03',
				'April': 	'04',
				'May': 		'05',
				'June': 	'06',
				'July': 	'07',
				'August': 	'08',
				'September':'09',
				'October':	'10',
				'November':	'11',
				'December':	'12'
		}

	return lookup[m]

def get_day_num(d):
	day_num = d[:len(d)-2]	# shaves off suffix 'st'|'nd'|'rd'|'th'
	if len(d)==3:
		day_num = '0' + day_num
	return day_num

# -------------------------------------------------- #
def get_db_starttime(msg):
	time_sig = get_time_signature(msg)
	db_starttime = return_starttime(time_sig)
	return db_starttime

def return_starttime(sig):
	return return_time(sig, 0)

# -------------------------------------------------- #
def get_db_endtime(msg):
	time_sig = get_time_signature(msg)
	db_endtime = return_endtime(time_sig)
	return db_endtime

def return_endtime(sig):
	return return_time(sig, 1)

# -------------------------------------------------- #
def get_time_signature(msg):
	tag = msg.find(DEMARC_KEY)
	msg = msg[tag:]			# advance past header info
	tag = msg.find('Time:')
	msg = msg[tag+5:]		# advance to date signature
	tag = msg.find('\n')
	sig = msg[:tag].strip()	# final date signature
	return sig

def return_time(sig, index):
	raw_time = sig.split(' - ')[index]
	colon = raw_time.find(':')
	h = int(raw_time[:colon])
	minutes = raw_time[colon+1:colon+3]
	am_pm = raw_time[colon+3:]
	h = (h + 12) if (('pm' in am_pm) or ('PM' in am_pm)) else h
	hour = ('0' + str(h)) if (h<10) else str(h)
	time = '%s:%s' % (hour, minutes)
	print time

	return time

# ========================================================== #
def handle_drop():
	f = open('CS419/CS419mail/proc_drop_output.txt', 'w')
	f.write(msg)
	f.close()
	return
# ========================================================== #
if __name__ == "__main__":

	main()
