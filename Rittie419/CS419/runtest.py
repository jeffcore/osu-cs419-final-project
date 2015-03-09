from db_funcs import view_appt, add_appt, drop_appt, new_table, drop_table
from db_funcs import is_repeat, get_unique_id

import add_appt, drop_appt
import add_calendar, drop_calendar
import send_conf_email
from procfilter import handle_add, get_date_signature, get_time_signature
from procfilter import return_date
import os
from datetime import datetime

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
'''

#add_calendar.add_calendar()
'''
drop_calendar.drop_calendar('Chuaprasert, Rittie', 
	'STUDENT',
	'chuaprar@engr.orst.edu', 
	datetime(2015,3,10,13,30),
	datetime(2015,3,10,14,45),
	'rixj@onid.orst.edu::2015-03-10::13:30')
'''
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



