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

CRLF = "\r\n"

# construct calendar header info
attendees = ["rittie@alumni-gsb.stanford.edu"]
organizer = "ORGANIZER;CN=Rittie Chuaprasert:mailto:chuaprar@engr.orst.edu"
fro = "Rittie <chuaprar@engr.orst.edu>"
description = "DESCRIPTION: test invitation from pyICSParser"+CRLF
attendee = ""
for att in attendees:
	attendee += "ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ PARTICIPANT;PARTSTAT=ACCEPTED;RSVP=TRUE"+CRLF
	attendee += " ;CN="+att+";X-NUM-GUESTS=0:"+CRLF
	attendee += " mailto:"+att+CRLF

# set calendar time signatures
ddtstart = datetime.datetime.now()
dtoff = datetime.timedelta(days = 1)
dur = datetime.timedelta(hours = 1)
ddtstart = ddtstart +dtoff
dtend = ddtstart + dur
dtstamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%SZ")
dtstart = ddtstart.strftime("%Y%m%dT%H%M%SZ")
dtend = dtend.strftime("%Y%m%dT%H%M%SZ")

# construct calendar item
ical = "BEGIN:VCALENDAR"+CRLF
ical+= "PRODID:pyICSParser"+CRLF
ical+= "VERSION:2.0"+CRLF
ical+= "CALSCALE:GREGORIAN"+CRLF
ical+= "METHOD:REQUEST"+CRLF
ical+= "BEGIN:VEVENT"+CRLF
ical+= "DTSTART:"+dtstart+CRLF
ical+= "DTEND:"+dtend+CRLF
ical+= "DTSTAMP:"+dtstamp+CRLF
ical+= organizer+CRLF
ical+= "UID:FIXMEUID"+dtstamp+CRLF
ical+= attendee+"CREATED:"+dtstamp+CRLF
ical+= description+"LAST-MODIFIED:"+dtstamp+CRLF
ical+= "LOCATION:"+CRLF
ical+= "SEQUENCE:0"+CRLF
ical+= "STATUS:CONFIRMED"+CRLF
ical+= "SUMMARY:test "+ddtstart.strftime("%Y%m%d @ %H:%M")+CRLF
ical+= "TRANSP:OPAQUE"+CRLF
ical+= "END:VEVENT"+CRLF
ical+= "END:VCALENDAR"+CRLF

# construct email headers and body
msg = MIMEMultipart('mixed')
msg['Reply-To'] = fro
msg['Date'] = formatdate(localtime=True)
msg['Subject'] = "pyICSParser invite"+dtstart
msg['From'] = fro
msg['To'] = ",".join(attendees)
eml_body = "Email body visible in the invite of outlook and outlook.com but not google calendar"

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
