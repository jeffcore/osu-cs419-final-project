'''
REFERENCE: http://stackoverflow.com/questions/4823574/sending-meeting-invitations-with-python
'''

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import formatdate
from email import Encoders
import os,datetime
from datetime import datetime

CRLF = "\r\n"

def drop_calendar(
	adv='Advisor Rittie', 
	stud='Student Rittie',
	adv_email='chuaprar@engr.orst.edu', 
	stud_email='rac42@cornell.edu',
	dt_start=datetime(2015,3,10,12,30),
	dt_end=datetime(2015,3,10,13,45), 
	uid='rac42@cornell.edu::2015-03-10::12:30'):

	# construct calendar header info
	attendees = [adv_email]
	organizer = "ORGANIZER;CN=%s:mailto:%s" % (adv, adv_email)
	fro = "%s <%s>" % (adv, adv_email)
	description = "DESCRIPTION: Advising Signup Cancellation"
	attendee = ""
	for att in attendees:
		attendee += "ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ PARTICIPANT;PARTSTAT=ACCEPTED;RSVP=TRUE"+CRLF
		attendee += " ;CN="+att+";X-NUM-GUESTS=0:"+CRLF
		attendee += " mailto:"+att+CRLF

	# set calendar time signatures
	dtstamp = datetime.now().strftime("%Y%m%dT%H%M%S")
	dtstart = dt_start.strftime("%Y%m%dT%H%M%S")
	dtend = dt_end.strftime("%Y%m%dT%H%M%S")
	datesuffix = get_date_suffix(int(dt_start.strftime("%d")))
	datetxt = dt_start.strftime("%A, %B %d") + datesuffix + dt_start.strftime(", %Y")
	starttxt = dt_start.strftime("%I:%M%p").replace('PM','pm').replace('AM','am').lstrip('0')
	endtxt = dt_end.strftime("%I:%M%p").replace('PM','pm').replace('AM','am').lstrip('0')

	# construct calendar item
	ical = "BEGIN:VCALENDAR"+CRLF
	ical+= "PRODID:CS419ADVISORPROJECT"+CRLF
	ical+= "VERSION:2.0"+CRLF
	ical+= "CALSCALE:GREGORIAN"+CRLF
	ical+= "METHOD:CANCEL"+CRLF
	ical+= "BEGIN:VEVENT"+CRLF
	ical+= "DTSTART:"+dtstart+CRLF
	ical+= "DTEND:"+dtend+CRLF
	ical+= "DTSTAMP:"+dtstamp+CRLF
	ical+= organizer+CRLF
	ical+= "UID:FIXMEUID"+uid+CRLF
	ical+= attendee+"CREATED:"+dtstamp+CRLF
	ical+= description+"LAST-MODIFIED:"+dtstamp+CRLF
	ical+= "LOCATION:"+CRLF
	ical+= "SEQUENCE:0"+CRLF
	ical+= "STATUS:CANCELLED"+CRLF
	ical+= "SUMMARY:Advising Signup CANCELLED"+CRLF
	ical+= "TRANSP:OPAQUE"+CRLF
	ical+= "END:VEVENT"+CRLF
	ical+= "END:VCALENDAR"+CRLF

	print '%s' % adv
	print '%s' % datetxt
	print '%s' % starttxt
	print '%s' % endtxt

	# construct email headers and body
	msg = MIMEMultipart('mixed')
	msg['Reply-To'] = fro
	msg['Date'] = formatdate(localtime=True)
	msg['Subject'] = "Advising Appointment with %s CANCELLED" % (stud)
	msg['From'] = fro
	msg['To'] = ",".join(attendees)
	eml_body = 	body = '''
	<br>Advising Signup with %s CANCELLED
	<br>Name: %s
	<br>Email: %s
	<br>Date: %s
	<br>Time: %s - %s


	<br><br><br>Please contact support@engr.oregonstate.edu if you experience problems
	''' % (adv, stud, stud_email, datetxt, starttxt, endtxt)
	print eml_body

	# declare multipart structure and content info
	msgAlternative = MIMEMultipart('alternative')
	msg.attach(msgAlternative)

	#	calendar content info
	part_cal = MIMEText(ical,'calendar;method=CANCEL')
	ical_atch = MIMEBase('application/ics',' ;name="%s"'%("invite.ics"))
	ical_atch.set_payload(ical)
	Encoders.encode_base64(ical_atch)
	ical_atch.add_header('Content-Disposition', 'attachment; filename="%s"'%("invite.ics"))

	#	email content info
	part_email = MIMEText(eml_body,"html")
	eml_atch = MIMEBase('text/plain','')
	Encoders.encode_base64(eml_atch)
	eml_atch.add_header('Content-Transfer-Encoding', "")

	msgAlternative.attach(part_cal)
	msgAlternative.attach(part_email)

	# send the email calendar invite
	mailServer = smtplib.SMTP('engr.orst.edu')

	# 	Put the SMTP connection in TLS (Transport Layer Security) mode
	mailServer.ehlo()
	mailServer.starttls()
	mailServer.ehlo()

	mailServer.sendmail(fro, attendees, msg.as_string())
	mailServer.close()

def get_date_suffix(d):
	lookup = {
		1:'st',	2:'nd',	3:'rd',	4:'th',	5:'th',
		6:'th',	7:'th',	8:'th',	9:'th',	10:'th',
		11:'th',12:'th',13:'th',14:'th',15:'th',
		16:'th',17:'th',18:'th',19:'th',20:'th',
		21:'st',22:'nd',23:'rd',24:'th',25:'th',
		26:'th',27:'th',28:'th',29:'th',30:'th',31:'st'
	}
	return lookup[d]

