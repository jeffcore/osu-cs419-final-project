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
	# handle cases of comment lines
	if ('#' in cmd):			# ignore inline text after comment tag
		comment_tag = cmd.find('#')
		cmd = cmd[0:comment_tag]	
	if	('-- ' in cmd) or ('--\n' in cmd) or	\
			('--\t' in cmd):	# ignore inline text after comment tag
		comment_tag = cmd.find('--')
		cmd = cmd[0:comment_tag]	
	while ('/*' in cmd):		# ignore text between comment tags
		while ('*/' not in cmd):
			cmd += gettext('')
		comment_tag1 = cmd.find('/*')
		comment_tag2 = cmd.find('*/') + 2
		cmd = cmd[0:comment_tag1] + cmd[comment_tag2:]

	# comment lines have been excluded
	fullcmd += cmd
	if ';' in fullcmd:
		print "(query >> '" + fullcmd + "')"
		print sql_cmd.execute(fullcmd);
		fullcmd = ''
		cmd = gettext('mysql419 >>')
	else:
		cmd = gettext('>>')

