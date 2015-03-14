'''
launcher.py
Group 8
Checks for the user's .procmailrc and .forward files. It creates the .procmailrc file if needed with the rules needed for the simplified advising system project.
Allows user to launch the CLI.
This file should be located in the user's main directory.
'''
import os
import sys
import imp
sys.path.append('./CS419')
import cursescli

procfile = ".procmailrc"
forward_file = ".forward"
menu_selection = 0
running = True

while running:
	print "\nWelcome to Group 8's Advising System Project!"
	print "Choose an option:\n\t1 Initial setup or Check configuration\n\t2 To run CLI\n\t3 To exit"
	print "Note, the system will not function properly if initial setup has not been completed."
	menu_selection = raw_input("Choose 1, 2, or 3: ")
	print "Choice was .... ", menu_selection

	if menu_selection == '1':
		if os.path.isfile(procfile):
			print "**********.procmailrc Message**********"
			print "Your .procmailrc file may need to be modified for the system to work."
			print "The required procmail rules can also be found in written instructions."
			
			print "The rules below are required,\nit is recommended to put them at the start of the file:\n"
			print ":0 fW:\n* ^From[: ].*do.not.reply@engr.orst.edu\n* ^Subject:.*Advising Signup\n| python ~/CS419/procfilter.py"
			print "\n:0\n* ^From[: ].*do.not.reply@engr.orst.edu\n* ^Subject:.*Advising Signup\n/dev/null"

			print "\nDo not include this line in the .procmailrc or anything below it."
			print "The rule must be included in the .procmailrc file for proper function!"
			print "***NOTE***If the .procmailrc file already contains the rules, you are good to go!"
		else:
			print "**********.procmailrc Message**********"
			print "Creating the required .procmailrc file..."
			
			userEmail = raw_input("Enter an email for forwarding: ")
			f = open('.procmailrc','w+')
			f.write("# A default .procmailrc file\n# See http://engr.oregonstate.edu/computing/email/90\n\n# Include the standard spam filter\nINCLUDERC=/usr/local/etc/procmail/standard.rc\n\n:0 fW:\n* ^From[: ].*do.not.reply@engr.orst.edu\n* ^Subject:.*Advising Signup\n| python ~/CS419/procfilter.py\n\n:0\n* ^From[: ].*do.not.reply@engr.orst.edu\n* ^Subject:.*Advising Signup\n/dev/null\n\n" + "# for other mail, forward everything\n:0\n* ^[a-zA-Z]+\n! " + userEmail)
			f.close()
		
			if os.path.isfile(procfile):
				print "Procmail setup complete!"
			else:
				print "Something went wrong with creating the .procmailrc file!"
			
		if os.path.isfile(forward_file):
			print"\n**********.forward Message**********"
			print "Your main directory contains a .forward file.\nThis will interfere with the advising system.\The file should be removed.\nThis can be completed using TEACH or manually removing the file from the directory."
			
	elif menu_selection == '2':
		if os.path.isfile(procfile):
			if not os.path.isfile(forward_file):
				#print "CLI Option"
				cursescli.main()
			else:
				print "*****Warning!*****\nThe .forward file will prevent proper functioning of the system.\nPlease remove the file to proceed.\nInformation can be found in:\n\t1. The Install Instruction text file\n\t2. Using Option 1 of this system."
		else:
			print "*****No .procmail file found!*****\nRun option 1 from the main menu."
		
	elif menu_selection == '3':
		print "Now exiting..."
		sys.exit(0)
		
	else:
		print "Invalid menu choice."