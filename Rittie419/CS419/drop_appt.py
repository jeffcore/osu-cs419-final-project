import sys
import smtplib
from datetime import datetime
from email.mime.text import MIMEText

def main(advisor='Chuaprasert, Rittie', 
	adv_email='chuaprar@engr.orst.edu', 
	dt_start=datetime(2015,3,10,12,30),
	dt_end=datetime(2015,3,10,13,45)):


	# prepare for date and time signatures	
	datetxt = dt_start.strftime("%A, %B %dth, %Y")
	starttxt = dt_start.strftime("%I:%M%p")
	endtxt = dt_end.strftime("%I:%M%p")

	body = '''
	Advising Signup with %s CANCELLED
	Name: REDACTED
	Email: REDACTED@engr.orst.edu
	Date: %s
	Time: %s - %s


	Please contact support@engr.oregonstate.edu if you experience problems
	''' % (advisor, datetxt, starttxt, endtxt)

	# Create plain text message
	msg = MIMEText(body)

	from_email = 'do.not.reply@engr.orst.edu'
	to_email = ['chuaprar@engr.orst.edu']
	cc_email = []
	#cc_email = ['kreuzigs@onid.orst.edu', 'rixj@onid.orst.edu', 'krullj@onid.orst.edu']
	msg['From'] = from_email
	msg['To'] = 'REDACTED@engr.orst.edu, ' + ','.join(to_email)
	msg['Cc'] = ','.join(cc_email)
	msg['Subject'] = "Advising Signup Cancellation"
	to_email.extend(cc_email)
	print to_email

	# send the message
	s = smtplib.SMTP('engr.orst.edu')
	s.sendmail(from_email, to_email, msg.as_string())
	s.quit

if __name__ == "__main__":

	main()
