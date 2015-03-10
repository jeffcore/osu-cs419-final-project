
print "This is to create the .procmailrc file. Any existing .procmailrc file will be overrode to this new one"
userEmail = raw_input("Enter your OSU email: ")

f = open('.procmailrc','w')
f.truncate()
f.write("# A default .procmailrc file\n# See http://engr.oregonstate.edu/computing/email/90\n\n# Include the standard spam filter\nINCLUDERC=/usr/local/etc/procmail/standard.rc\n\n####################################################\n# (Optionally) Add your own rules after this line\n####################################################\n\n:0 fW:\n* ^From[: ].*do.not.reply@engr.orst.edu\n* ^Subject:.*Advising Signup\n| python ~/CS419/procfilter.py\n\n:0\n* ^From[: ].*do.not.reply@engr.orst.edu\n* ^Subject:.*Advising Signup\nCS419/CS419mail/. CS419/CS419mail/newmail.txt\n\n:0 cB\n* ^BEGIN:VCALENDAR\nCS419/CS419mail/ical/.\n\n# for other mail, forward everything to OSU gmail\n:0\n* ^[a-zA-Z]+\n! " + userEmail+"\n\n:0\nCS419/CS419mail/spam/.\n\n")
f.close()