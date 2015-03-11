from db_funcs import view_appt, add_appt, drop_appt, new_table, drop_table
from db_funcs import is_repeat, get_unique_id

import add_appt, drop_appt
import add_calendar, drop_calendar
import send_conf_email
import procfilter
from procfilter import handle_add, get_date_signature, get_time_signature
from procfilter import return_date
import os
from datetime import datetime
from testtools import get_plaintext_add_appt, get_plaintext_drop_appt
def main():
	procfilter_tests()
	#calendar_tests()

def procfilter_tests():
	#####-----<PROC FILTER TESTS>-----------------#####
	currtestnum = 0
	###------<UNIT TESTS>-----------###
	adv = 'Test Adviser_Name'
	stud = 'Test Student_Name'
	adv_email = 'Test Adviser_Email'
	stud_email = 'Test Student_Email'
	dt_start = datetime(2015,4,21,13,30)
	dt_end = datetime(2015,4,21,14,45)
	date_sig = 'Tuesday, April 21st, 2015'
	time_sig = '1:30pm - 2:45pm'
	plaintext_add = get_plaintext_add_appt(adv,adv_email,stud,stud_email,dt_start,dt_end)
	#print plaintext_add
	plaintext_drop = get_plaintext_drop_appt(adv,adv_email,stud,stud_email,dt_start,dt_end)
	#print plaintext_drop
	#----------------------------------#
	currtest = 'procfilter.get_db_advisor_add()'
	currtestnum = currtestnum + 1
	targtext = adv
	assert targtext==procfilter.get_db_advisor_add(plaintext_add), "FAILED %d" %currtestnum

	print 'PASSED: procfiltertest #%d: %s' % (currtestnum, currtest)

	#----------------------------------#
	currtest = 'procfilter.get_db_student()'
	currtestnum = currtestnum + 1
	#print stud
	#print procfilter.get_db_student(plaintext_add)
	targtext = stud
	assert targtext==procfilter.get_db_student(plaintext_add), "FAILED %d" %currtestnum

	print 'PASSED: procfiltertest #%d: %s' % (currtestnum, currtest)

	#----------------------------------#
	currtest = 'procfilter.get_db_advisor_email()'
	currtestnum = currtestnum + 1
	targtext = adv_email
	assert targtext==procfilter.get_db_advisor_email(plaintext_add), "FAILED %d" %currtestnum

	print 'PASSED: procfiltertest #%d: %s' % (currtestnum, currtest)

	#----------------------------------#
	currtest = 'procfilter.get_db_student_email()'
	currtestnum = currtestnum + 1
	targtext = stud_email
	assert targtext==procfilter.get_db_student_email(plaintext_add), "FAILED %d" %currtestnum

	print 'PASSED: procfiltertest #%d: %s' % (currtestnum, currtest)

	#----------------------------------#
	currtest = 'procfilter.findtext()'
	currtestnum = currtestnum + 1
	key1 = 'From:'
	key2 = 'To:'
	targtext = 'do.not.reply@engr.orst.edu'
	assert targtext==procfilter.findtext(plaintext_add, key1, key2), "FAILED %d" %currtestnum
	key1 = 'Content-Type:'
	key2 = 'charset="us-ascii"'
	targtext = 'text/plain;'
	assert targtext==procfilter.findtext(plaintext_add, key1, key2), "FAILED %d" %currtestnum

	print 'PASSED: procfiltertest #%d: %s' % (currtestnum, currtest)

	#----------------------------------#
	currtest = 'procfilter.get_month_num()'
	currtestnum = currtestnum + 1
	montharray = ['January','February','March','April','May','June',
		'July','August','September','October','November','December']
	for i in range(12):
		targtext = str(i+1) if (i>=9) else '0' + str(i+1)
		#print targtext, montharray[i]
		assert targtext==procfilter.get_month_num(montharray[i]), "FAILED %d" %currtestnum

	print 'PASSED: procfiltertest #%d: %s' % (currtestnum, currtest)

	#----------------------------------#
	currtest = 'procfilter.get_day_num()'
	currtestnum = currtestnum + 1
	days = ['1st', '1', '22nd', '22', '3rd', '3', '10th', '10', '31st', '31']
	targs = ['01', '01', '22', '22', '03', '03', '10', '10', '31', '31']
	for i in range(10):
		d = days[i]
		targtext = targs[i]
		assert targtext==procfilter.get_day_num(d), "FAILED %d" %currtestnum

	print 'PASSED: procfiltertest #%d: %s' % (currtestnum, currtest)

	#----------------------------------#
	currtest = 'procfilter.get_date_signature()'
	currtestnum = currtestnum + 1
	dt_start = datetime(2015,4,21,13,30)
	dt_end = datetime(2015,4,21,14,45)
	date_sig = 'Tuesday, April 21st, 2015'
	plaintext_add = get_plaintext_add_appt(adv,adv_email,stud,stud_email,dt_start,dt_end)
	targtext = date_sig
	assert targtext==procfilter.get_date_signature(plaintext_add), "FAILED %d" %currtestnum
	#------------------
	dt_start = datetime(2015,12,23,13,30)
	dt_end = datetime(2015,12,23,14,45)
	date_sig = 'Wednesday, December 23rd, 2015'
	plaintext_add = get_plaintext_add_appt(adv,adv_email,stud,stud_email,dt_start,dt_end)
	targtext = date_sig
	assert targtext==procfilter.get_date_signature(plaintext_add), "FAILED %d" %currtestnum

	print 'PASSED: procfiltertest #%d: %s' % (currtestnum, currtest)

	#----------------------------------#
	currtest = 'procfilter.return_date()'
	currtestnum = currtestnum + 1
	date_sig = 'Tuesday, April 21st, 2015'
	targtext = '2015-04-21'
	assert targtext==procfilter.return_date(date_sig), "FAILED %d" %currtestnum
	date_sig = 'Wednesday, December 23rd, 2015'
	targtext = '2015-12-23'
	assert targtext==procfilter.return_date(date_sig), "FAILED %d" %currtestnum

	print 'PASSED: procfiltertest #%d: %s' % (currtestnum, currtest)

	#----------------------------------#
	currtest = 'procfilter.get_db_date()'
	currtestnum = currtestnum + 1
	dt_start = datetime(2015,4,21,13,30)
	dt_end = datetime(2015,4,21,14,45)
	date_sig = 'Tuesday, April 21st, 2015'
	plaintext_add = get_plaintext_add_appt(adv,adv_email,stud,stud_email,dt_start,dt_end)
	targtext = '2015-04-21'
	assert targtext==procfilter.get_db_date(plaintext_add), "FAILED %d" %currtestnum
	#------------------
	dt_start = datetime(2015,12,23,13,30)
	dt_end = datetime(2015,12,23,14,45)
	date_sig = 'Wednesday, December 23rd, 2015'
	plaintext_add = get_plaintext_add_appt(adv,adv_email,stud,stud_email,dt_start,dt_end)
	targtext = '2015-12-23'
	assert targtext==procfilter.get_db_date(plaintext_add), "FAILED %d" %currtestnum

	print 'PASSED: procfiltertest #%d: %s' % (currtestnum, currtest)

	#----------------------------------#
	currtest = 'procfilter.get_time_signature()'
	currtestnum = currtestnum + 1
	dt_start = datetime(2015,4,21,13,30)
	dt_end = datetime(2015,4,21,14,45)
	time_sig = '1:30pm - 2:45pm'
	plaintext_add = get_plaintext_add_appt(adv,adv_email,stud,stud_email,dt_start,dt_end)
	targtext = time_sig
	assert targtext==procfilter.get_time_signature(plaintext_add), "FAILED %d" %currtestnum
	#------------------
	dt_start = datetime(2015,4,21,9,10)
	dt_end = datetime(2015,4,21,10,00)
	time_sig = '9:10am - 10:00am'
	plaintext_add = get_plaintext_add_appt(adv,adv_email,stud,stud_email,dt_start,dt_end)
	targtext = time_sig
	assert targtext==procfilter.get_time_signature(plaintext_add), "FAILED %d" %currtestnum

	print 'PASSED: procfiltertest #%d: %s' % (currtestnum, currtest)
	#----------------------------------#
	currtest = 'procfilter.return_time(sig, index)'
	currtestnum = currtestnum + 1
	dt_start = datetime(2015,4,21,13,30)
	dt_end = datetime(2015,4,21,14,45)
	time_sig = '1:30pm - 2:45pm'
	plaintext_add = get_plaintext_add_appt(adv,adv_email,stud,stud_email,dt_start,dt_end)
	index = 0
	targtext = '13:30'
	assert targtext==procfilter.return_time(time_sig, index), "FAILED %d" %currtestnum
	#------------------
	index = 1
	targtext = '14:45'
	assert targtext==procfilter.return_time(time_sig, index), "FAILED %d" %currtestnum
	#------------------
	dt_start = datetime(2015,4,21,9,10)
	dt_end = datetime(2015,4,21,10,00)
	time_sig = '9:10am - 10:00am'
	plaintext_add = get_plaintext_add_appt(adv,adv_email,stud,stud_email,dt_start,dt_end)
	index = 0
	targtext = '09:10'
	assert targtext==procfilter.return_time(time_sig, index), "FAILED %d" %currtestnum
	#------------------
	index = 1
	targtext = '10:00'
	assert targtext==procfilter.return_time(time_sig, index), "FAILED %d" %currtestnum

	print 'PASSED: procfiltertest #%d: %s' % (currtestnum, currtest)
	#----------------------------------#
	currtest = 'procfilter.return_starttime()'
	currtestnum = currtestnum + 1
	time_sig = '1:30pm - 2:45pm'
	targtext = '13:30'
	assert targtext==procfilter.return_starttime(time_sig), "FAILED %d" %currtestnum
	#------------------
	time_sig = '9:10am - 10:00am'
	targtext = '09:10'
	assert targtext==procfilter.return_starttime(time_sig), "FAILED %d" %currtestnum

	print 'PASSED: procfiltertest #%d: %s' % (currtestnum, currtest)

	#----------------------------------#
	currtest = 'procfilter.return_endtime()'
	currtestnum = currtestnum + 1
	time_sig = '1:30pm - 2:45pm'
	targtext = '14:45'
	assert targtext==procfilter.return_endtime(time_sig), "FAILED %d" %currtestnum
	#------------------
	time_sig = '9:10am - 10:00am'
	targtext = '10:00'
	assert targtext==procfilter.return_endtime(time_sig), "FAILED %d" %currtestnum

	print 'PASSED: procfiltertest #%d: %s' % (currtestnum, currtest)

	#----------------------------------#
	currtest = 'procfilter.get_db_starttime()'
	currtestnum = currtestnum + 1
	dt_start = datetime(2015,4,21,13,30)
	dt_end = datetime(2015,4,21,14,45)
	plaintext_add = get_plaintext_add_appt(adv,adv_email,stud,stud_email,dt_start,dt_end)
	targtext = '13:30'
	assert targtext==procfilter.get_db_starttime(plaintext_add), "FAILED %d" %currtestnum
	#------------------
	dt_start = datetime(2015,4,21,9,10)
	dt_end = datetime(2015,4,21,10,00)
	plaintext_add = get_plaintext_add_appt(adv,adv_email,stud,stud_email,dt_start,dt_end)
	targtext = '09:10'
	assert targtext==procfilter.get_db_starttime(plaintext_add), "FAILED %d" %currtestnum

	print 'PASSED: procfiltertest #%d: %s' % (currtestnum, currtest)

	#----------------------------------#
	currtest = 'procfilter.get_db_endtime()'
	currtestnum = currtestnum + 1
	dt_start = datetime(2015,4,21,13,30)
	dt_end = datetime(2015,4,21,14,45)
	plaintext_add = get_plaintext_add_appt(adv,adv_email,stud,stud_email,dt_start,dt_end)
	targtext = '14:45'
	assert targtext==procfilter.get_db_endtime(plaintext_add), "FAILED %d" %currtestnum
	#------------------
	dt_start = datetime(2015,4,21,9,10)
	dt_end = datetime(2015,4,21,10,00)
	plaintext_add = get_plaintext_add_appt(adv,adv_email,stud,stud_email,dt_start,dt_end)
	targtext = '10:00'
	assert targtext==procfilter.get_db_endtime(plaintext_add), "FAILED %d" %currtestnum

	print 'PASSED: procfiltertest #%d: %s' % (currtestnum, currtest)

	#----------------------------------#
	currtest = 'procfilter.get_db_advisor_drop()'
	currtestnum = currtestnum + 1
	targtext = adv
	assert targtext==procfilter.get_db_advisor_drop(plaintext_drop), "FAILED %d" %currtestnum

	print 'PASSED: procfiltertest #%d: %s' % (currtestnum, currtest)

	#----------------------------------#
	currtest = 'procfilter.get_dt(db_date, db_start)'
	currtestnum = currtestnum + 1
	db_date = '2015-04-21'
	db_start = '13:30'
	targdt = datetime(2015,4,21,13,30)
	assert targdt==procfilter.get_dt(db_date, db_start), "FAILED %d" %currtestnum
	#------------------
	db_date = '2015-04-21'
	db_start = '09:10'
	targdt = datetime(2015,4,21,9,10)
	assert targdt==procfilter.get_dt(db_date, db_start), "FAILED %d" %currtestnum

	print 'PASSED: procfiltertest #%d: %s' % (currtestnum, currtest)

	#----------------------------------#
	currtest = 'procfilter.get_db_student_email()'
	currtestnum = currtestnum + 1
	#assert targtext==procfilter.get_db_student_email(plaintext_add), "FAILED %d" %currtestnum
	#print 'PASSED: procfiltertest #%d: %s' % (currtestnum, currtest)
	#----------------------------------#
	currtest = 'procfilter.get_db_student_email()'
	currtestnum = currtestnum + 1
	#assert targtext==procfilter.get_db_student_email(plaintext_add), "FAILED %d" %currtestnum
	#print 'PASSED: procfiltertest #%d: %s' % (currtestnum, currtest)

	print "DONE"
	###------<USER STORY TESTS>-----------###
	#add_appt.main()
	'''
	add_appt.main('Advisor Rittie2', 
		'chuaprar@engr.orst.edu', 
		'Student Rittie2',
		'rittie@alumni-gsb.stanford.edu',
		datetime(2015,3,10,13,30),
		datetime(2015,3,10,14,45))
	'''
	'''
	drop_appt.main('Advisor Rittie2', 
		'chuaprar@engr.orst.edu', 
		'Student Rittie2',
		'rittie@alumni-gsb.stanford.edu',
		datetime(2015,3,10,13,30),
		datetime(2015,3,10,14,45))
	'''
	'''
	add_appt.main('Advisor Rittie', 
		'chuaprar@engr.orst.edu', 
		'Student Rittie',
		'rac42@cornell.edu',
		datetime(2015,3,10,10,30),
		datetime(2015,3,10,11,45))
	'''
	'''
	drop_appt.main('Advisor Rittie', 
		'chuaprar@engr.orst.edu', 
		'Student Rittie',
		'rac42@cornell.edu',
		datetime(2015,3,10,10,30),
		datetime(2015,3,10,11,45))
	'''
	'''
	add_appt.main('Advisor Rittie', 
		'chuaprar@engr.orst.edu', 
		'Student 3',
		'rac42@cornell.edu',
		datetime(2015,3,11,10,30),
		datetime(2015,3,11,11,45))
	'''
	'''
	drop_appt.main('Advisor Rittie', 
		'chuaprar@engr.orst.edu', 
		'Student 3',
		'rac42@cornell.edu',
		datetime(2015,3,11,10,30),
		datetime(2015,3,11,11,45))
	'''
	pass

from procfilter import get_day_num
def calendar_tests():
	#add_calendar.add_calendar()
	'''
	drop_calendar.drop_calendar('Chuaprasert, Rittie', 
		'STUDENT',
		'chuaprar@engr.orst.edu', 
		datetime(2015,3,10,13,30),
		datetime(2015,3,10,14,45),
		'rixj@onid.orst.edu::2015-03-10::13:30')
	'''

	for i in range(1,32):
		suffix = get_date_suffix(i)
		day_of_month = str(i)
		print "%s -> %s" %(day_of_month, get_day_num(day_of_month))
		day_of_month = str(i) + suffix
		print "%s -> %s" %(day_of_month, get_day_num(day_of_month))

	dt_start=datetime(2015,3,10,12,30)
	print dt_start.strftime("%d")
	datesuffix = get_date_suffix(int(dt_start.strftime("%d")))
	print datesuffix
	datesuffix = add_calendar.get_date_suffix(int(dt_start.strftime("%d")))
	print datesuffix
	datetxt = dt_start.strftime("%A, %B %d") + datesuffix + dt_start.strftime(", %Y")
	print datetxt

def get_date_suffix(d):
	lookup = {
		1:'st',
		2:'nd',
		3:'rd',
		4:'th',
		5:'th',
		6:'th',
		7:'th',
		8:'th',
		9:'th',
		10:'th',
		11:'th',
		12:'th',
		13:'th',
		14:'th',
		15:'th',
		16:'th',
		17:'th',
		18:'th',
		19:'th',
		20:'th',
		21:'st',
		22:'nd',
		23:'rd',
		24:'th',
		25:'th',
		26:'th',
		27:'th',
		28:'th',
		29:'th',
		30:'th',
		31:'st'
	}
	return lookup[d]


#add_appt.main()
#send_conf_email.main()
#send_conf_email.main(mtg_type='CANCELLED')
#send_conf_email.main(mtg_type='jgdjg')
# <---------------------------------------------> #
'''
os.chdir('..')
print os.getcwd()
f = open('CS419/CS419mail/proc_add_output.txt', 'r')
msg = f.read()
#print msg
handle_add(msg)
'''
# <---------------------------------------------> #
'''
os.chdir('..')
print os.getcwd()
f = open('CS419/CS419mail/1', 'r')
msg = f.read()
print msg
print get_date_signature(msg)
sig = get_date_signature(msg)
print return_date(sig)

print get_time_signature(msg)
'''
# <---------------------------------------------> #



#####-----<DATABASE TESTS>--------------------#####
#	 create blank table in database
#new_table('new_table_test')
#new_table('appointment')
# 	drop a database table
#drop_table('new_table_test')
# <---------------------------------------------> #
#print view_appt()
# <---------------------------------------------> #

'''
for i in range(100):
	add_appt("Jeff Rix%s" % i, "Rittie Chuaprasert",
	"rixj@onid.oregonstate.edu", "chuaprar@onid.oregonstate.edu",
	"2015-02-09", "11:00:00", "11:30:00")
'''
# <---------------------------------------------> #
'''
flag=1
if flag:
	unique_id =  add_appt("Jeff Rix999", "Rittie Chuaprasert",
	"rixj@onid.oregonstate.edu", "chuaprar@onid.oregonstate.edu",
	"2015-02-09", "11:30:00", "13:45:00")
	print unique_id
else:
	unique_id =  drop_appt("2015-02-09", "11:30:00")
	print unique_id
'''
# <---------------------------------------------> #
#print is_repeat("2015-02-09", "11:00:00", "12:00:01")

# <---------------------------------------------> #
#print get_unique_id("2015-02-09", "11:30:00")

if __name__ == "__main__":

	main()

