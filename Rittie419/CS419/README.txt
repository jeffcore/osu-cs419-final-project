This folder ('CS419') is the main hub for CS419-W15-Group8 PROJECT: Simplified Advising Scheduling.
It contains all the .py source code for the project.

For the application to be operational, this folder must reside on engr.oregonstate.edu in the user's main directory ('~/') along with ~/.procmailrc file, so this directory path is ~/CS419.

Description of modules:
add_appt.py - sends plain text email in format of advisor system
add_calendar.py - sends Outlook calendar invite for new appointment adds
drop_appt.py - sends plain text email in format of advisor system
drop_calendar.py - sends Outlook calendar cancellation of previously scheduled appointment
db_funcs.py - performs database functions executed as part of the project
get_email.py - given OSU student name, finds the student's email address
mysql419.py - CLI tool to interface with cs419-g8 database (similar to MySQL via CLI)
procfilter.py - receives plain text email from .procmailrc and completes scheduling tasks
runtest.py - contains tests of various project components / sub-systems
send_conf_email.py - sends appropriate confirmation email to student, either a CONFIRM or CANCEL
sql_cmd.py - executes MySQL queries in cs419-g8 database

Makefile: currently just removes *.pyc files with 'make clean'

CS419mail (~/CS419/CS419mail) directory: stores diagnostic information about application runs.
