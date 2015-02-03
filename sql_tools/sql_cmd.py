'''
This tool implements a MySQL command on the CS419 group8 database.
It is a self-contained function meant to be called by other scripts.

To use this tool within another python script: 
	import sql_cmd
	syntax: 'sql_cmd.execute(query)' where query = MySQL query text string
	example: assigning sql_cmd result to variable sql_result:
		sql_result = sql_cmd.execute(query)
'''

import subprocess

# executes a given MySQL command on cs419-g8 database
# @param query	MySQL command to be executed
# @return if applicable, returns any output from MySQL command
def execute(query):

	# prepares linux shell command to perform MySQL query
	query = 'USE cs419-g8;\n' + query
	authen = '-u cs419-g8 --password=9bWxwfvCAqUncYZV'
	server = '-h mysql.eecs.oregonstate.edu'
	linux_cmd = "mysql %s %s -t -e '%s' " % (authen, server, query)

	# executes MySQL query from linux shell command and stores output
	output = subprocess.Popen(linux_cmd, 
		shell=True, stdout=subprocess.PIPE).communicate()[0]

	return output
