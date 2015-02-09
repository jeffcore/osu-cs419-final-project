import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

import getpass

from_email = raw_input('enter username:')
to_email = 'rac42@cornell.edu'
pw = getpass.getpass('enter password:')

msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = 'simple email in python'
message = 'here is the email'
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp.gmail.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login(from_email, pw)

mailserver.sendmail(from_email, [to_email], msg.as_string())

mailserver.quit()
