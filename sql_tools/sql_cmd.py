'''
This tool implements a MySQL command on the CS419 group8 database.
It is a self-contained function meant to be called by other scripts.

To use this tool within another python script: 
	import sql_cmd
	syntax: 'sql_cmd.execute(query, borders)' where 
		query = MySQL query text string
		borders = (True = table borders; False = data output only) 
	example: assigning sql_cmd result to variable sql_result:
		sql_result = sql_cmd.execute(query, False)
'''

import subprocess

# executes a given MySQL command on cs419-g8 database
# @param query	MySQL command to be executed
# @return if applicable, returns any output from MySQL command
def execute(query, borders=True):

	# prepares linux shell command to perform MySQL query
	query = 'USE cs419-g8;\n' + query
	authen = '-u cs419-g8 %s' % blrr()
	server = '-h mysql.eecs.oregonstate.edu'
	border = '-t --raw' if borders else '--batch --raw --silent'
	linux_cmd = "mysql %s %s %s -e '%s' " % (authen, server, border, query)

	# executes MySQL query from linux shell command and stores output
	output = subprocess.Popen(linux_cmd, 
		shell=True, stdout=subprocess.PIPE).communicate()[0]

	return output

def blrr():
	tray = []
	baton = ""
	base=2
	lucky=7
	exp=3
	nudge = base**exp*lucky
	tray.append(int(chr(nudge)) + 37)
	tray.append(int(chr(nudge)) + 37)
	tray.append(int(chr(nudge)) + 104)
	tray.append(int(chr(nudge)) + 89)
	tray.append(int(chr(nudge)) + 107)
	tray.append(int(chr(nudge)) + 107)
	tray.append(int(chr(nudge)) + 111)
	tray.append(int(chr(nudge)) + 103)
	tray.append(int(chr(nudge)) + 106)
	tray.append(int(chr(nudge)) + 92)
	tray.append(int(chr(nudge)) + 53)
	tray.append(int(chr(nudge)) + 49)
	tray.append(int(chr(nudge)) + 90)
	tray.append(int(chr(nudge)) + 79)
	tray.append(int(chr(nudge)) + 112)
	tray.append(int(chr(nudge)) + 111)
	tray.append(int(chr(nudge)) + 94)
	tray.append(int(chr(nudge)) + 110)
	tray.append(int(chr(nudge)) + 59)
	tray.append(int(chr(nudge)) + 57)
	tray.append(int(chr(nudge)) + 105)
	tray.append(int(chr(nudge)) + 77)
	tray.append(int(chr(nudge)) + 102)
	tray.append(int(chr(nudge)) + 91)
	tray.append(int(chr(nudge)) + 81)
	tray.append(int(chr(nudge)) + 82)
	tray.append(int(chr(nudge)) + 78)
	for x in range(len(tray)):
		baton += chr(tray[x])
	return baton

