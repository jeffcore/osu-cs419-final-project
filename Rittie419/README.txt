I'm posting my entire CS419 runtime and testing environment that I use on FLIP.  Test cases for receiving a new appointment email and receiving an appointment cancellation email work all the way through the system, i.e. it routes through .procmailrc, filters the email to extract data, updates the database, sends a working Outlook calendar item with a reproduceable unique ID, and sends appointment confirmation email to student.

See ~/CS419/README.txt for more information about key .py modules.

On FLIP I have this CS419 in my user directory (path = ~/CS419) which is the same folder where .procmailrc resides.

--Rittie
