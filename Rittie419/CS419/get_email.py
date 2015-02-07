'''
Program:	get_email.py

Description: 
	Given a student name, the program searches for the name in
	directory.oregonstate.edu and outputs the emails of any student matches.

Usage:	shell command = 'python get_email.py ["Search Name"]'

Working Examples:	
	python get_email.py "Brabham, Matthew Lawrence"
	python get_email.py
	python get_email.py "Jeff Rix"
	python get_email.py "Rittie"
	python get_email.py "David, John"
	python get_email.py kreuziger

Notes: 
	- Set global variable fyi_message_on=True for more runtime diagnostics
	- The program will produce file output.txt containing the raw search 
		directory html source in the current directory.
'''

import sys, getopt, subprocess
fyi_messages_on = False

def main(argv):
	defaultname = 'Brabham, Matthew Lawrence'

	if len(argv)==1:
		rawname = argv[0]
	else:
		rawname = defaultname
	
	search_url = get_search_url(rawname)
	html = get_html_searchresult(search_url)
	emails = extract_emails(html)
	print 'result emails:\t', emails
	
	if len(emails)==1:
		return emails[0]
	else:
		return 

# @param rawname = directory search input
# @return directory search url
def get_search_url(rawname):
	# initialize start of search url
	url_start = 'http://directory.oregonstate.edu/?type=search&cn='

	if fyi_messages_on:
		print 'CLI arg:\t', rawname

	parsedname = rawname.replace(',',' ').split()
	if fyi_messages_on:
		print 'parsed name:\t', parsedname

	searchname = '+'.join(parsedname)
	if fyi_messages_on:
		print 'search name:\t', searchname

	url = url_start + searchname
	if fyi_messages_on:
		print 'search url:\t', url

	return url

# @param url = directory search url
# @return html source returned from directory.oregonstate.edu
def get_html_searchresult(url):
	linux_cmd = 	'(curl -s "' + url + '")'	# gets entire search html
	#linux_cmd +=	'| (grep "mailto:")'		# filters on lines with 'mailto:'
	linux_cmd +=	'| (tee ./output.txt)'		# outputs cmd result to text file
	if fyi_messages_on:
		print 'linux cmd:\t', linux_cmd
	## this would be ideal but is new for python 2.7; OSU uses 2.6.6 :(
	## html = subprocess.check_output(linux_cmd, shell=True)
	html = subprocess.Popen(linux_cmd, shell=True, stdout=subprocess.PIPE).communicate()[0]
	if fyi_messages_on:
		print 'len(html):\t', len(html)
	return html

# @param html = html source returned from directory.oregonstate.edu
# @return array of any emails extracted from directory search html
def extract_emails(html):
	emailcount = html.count('mailto:')
	print 'email count:\t', emailcount

	emails = []
	charindex = 0
	for i in range(emailcount):
		this_mailto_index = html.find('mailto:', charindex, len(html))
		beg_marker = this_mailto_index + len('mailto:')
		end_marker = html.find('"', beg_marker, len(html))
		this_email = html[beg_marker:end_marker]
		this_email = this_email.replace('&#046;','.').replace('&#064;','@')
		print '\t' + this_email		
		#print i, this_mailto_index, beg_marker, end_marker, this_email
		
		emails.append(this_email)
		charindex = end_marker
	return emails


if __name__ == "__main__":

	main(sys.argv[1:])
