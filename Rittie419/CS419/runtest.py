from db_funcs import view_appt, add_appt, drop_appt, new_table, drop_table
from db_funcs import is_repeat, get_unique_id

import add_appt, drop_appt
import add_calendar, drop_calendar
import send_conf_email
from procfilter import handle_add, get_date_signature, get_time_signature
from procfilter import return_date
import os
from datetime import datetime

def main():
	procfilter_tests()
	#calendar_tests()

def procfilter_tests():
	#####-----<PROC FILTER TESTS>-----------------#####

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
	
	drop_appt.main('Advisor Rittie', 
		'chuaprar@engr.orst.edu', 
		'Student 3',
		'rac42@cornell.edu',
		datetime(2015,3,11,10,30),
		datetime(2015,3,11,11,45))
	
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

