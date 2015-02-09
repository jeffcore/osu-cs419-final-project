
import smtplib

from email.mime.text import MIMEText

# Create plain text message
msg = MIMEText("Testing Testing - hello there!")

from_email = 'rixj@engr.orst.edu'
to_email = 'rac42@cornell.edu'
msg['Subject'] = 'Test email #1'
msg['From'] = from_email
msg['To'] = to_email


# send the message
s = smtplib.SMTP('engr.orst.edu')
s.sendmail(from_email, [to_email], msg.as_string())
s.quit

