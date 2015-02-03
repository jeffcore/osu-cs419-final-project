'''
To RUN this tool, type at the command prompt:
	python mysql419.py

This tool emulates a live MySQL console applied to the cs419-g8 database.
At runtime, user gets a prompt 'mysql419 >> '
Enter a MySQL query at the prompt.

Any input containing ';' will mark the end of a query and be executed.
Until an input contains ';' any new text is added to a query being constructed.
You may add multi-line queries and multiple queries at the same time.  The 
program will execute the queries sequentially.

To EXIT, enter 'exit' at the prompt.
'''

import sql_cmd

def gettext(prompt):
	result = raw_input(prompt)
	return result

fullcmd = ''
cmd = gettext('mysql419 >>')
while (cmd != 'exit'):
	fullcmd += cmd
	if ';' in fullcmd:
		print "(query >> '" + fullcmd + "')"
		print sql_cmd.execute(fullcmd);
		fullcmd = ''
		cmd = gettext('mysql419 >>')
	else:
		cmd = gettext('>>')

