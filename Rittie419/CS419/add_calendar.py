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

def add_calendar(
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
	description = "DESCRIPTION: Advisor Appointment with %s" % (stud)+CRLF
	attendee = ""
	for att in attendees:
		attendee += "ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ PARTICIPANT;PARTSTAT=ACCEPTED;RSVP=TRUE"+CRLF
		attendee += " ;CN="+att+";X-NUM-GUESTS=0:"+CRLF
		attendee += " mailto:"+att+CRLF

	# set calendar time signatures
	dtstamp = datetime.now().strftime("%Y%m%dT%H%M%S")
	dtstart = dt_start.strftime("%Y%m%dT%H%M%S")
	dtend = dt_end.strftime("%Y%m%dT%H%M%S")
	datetxt = dt_start.strftime("%A, %B %d, %Y")
	starttxt = dt_start.strftime("%I:%M%p")
	endtxt = dt_end.strftime("%I:%M%p")

	# construct calendar item
	ical = "BEGIN:VCALENDAR"+CRLF
	ical+= "PRODID:CS419ADVISORPROJECT"+CRLF
	ical+= "VERSION:2.0"+CRLF
	ical+= "CALSCALE:GREGORIAN"+CRLF
	ical+= "METHOD:REQUEST"+CRLF
	ical+= "BEGIN:VEVENT"+CRLF
	ical+= "DTSTART:"+dtstart+CRLF
	ical+= "DTEND:"+dtend+CRLF
	ical+= "DTSTAMP:"+dtstamp+CRLF
	ical+= organizer+CRLF
	ical+= "UID:FIXMEUID"+uid+CRLF
	ical+= attendee+"CREATED:"+dtstamp+CRLF
	ical+= description+"LAST-MODIFIED:"+dtstamp+CRLF
	ical+= "LOCATION: Student to contact Advisor"+CRLF
	ical+= "SEQUENCE:0"+CRLF
	ical+= "STATUS:CONFIRMED"+CRLF
	ical+= "SUMMARY:Advisor Signup with %s confirmed for %s" % (adv, stud)+CRLF
	ical+= "TRANSP:OPAQUE"+CRLF
	ical+= "END:VEVENT"+CRLF
	ical+= "END:VCALENDAR"+CRLF

	# construct email headers and body
	msg = MIMEMultipart('mixed')
	msg['Reply-To'] = fro
	msg['Date'] = formatdate(localtime=True)
	msg['Subject'] = "Advisor Appointment with %s" % (stud)
	msg['From'] = fro
	msg['To'] = ",".join(attendees)
	eml_body = 	body = '''
	<br>Advising Signup with %s confirmed
	<br>Name: %s
	<br>Email: %s
	<br>Date: %s
	<br>Time: %s - %s


	<br><br><br>Please contact support@engr.oregonstate.edu if you experience problems
	''' % (adv, stud, stud_email, datetxt, starttxt, endtxt)

	# declare multipart structure and content info
	msgAlternative = MIMEMultipart('alternative')
	msg.attach(msgAlternative)

	#	calendar content info
	part_cal = MIMEText(ical,'calendar;method=REQUEST')
	ical_atch = MIMEBase('application/ics',' ;name="%s"'%("invite.ics"))
	ical_atch.set_payload(ical)
	Encoders.encode_base64(ical_atch)
	ical_atch.add_header('Content-Disposition', 'attachment; filename="%s"'%("invite.ics"))

	#	email content info
	part_email = MIMEText(eml_body,'html')
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
