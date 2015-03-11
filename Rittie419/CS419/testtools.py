from datetime import datetime

def get_plaintext_add_appt(advisor='Advisor Chuaprasert, Rittie', 
	adv_email='chuaprar@engr.orst.edu', 
	student='Student Rix, Jeffrey Allan',
	stud_email='rixempire@gmail.com',
	dt_start=datetime(2015,3,10,12,30),
	dt_end=datetime(2015,3,10,13,45)):

	# prepare for date and time signatures	
	datesuffix = get_date_suffix(int(dt_start.strftime("%d")))
	datetxt = dt_start.strftime("%A, %B %d") + datesuffix + dt_start.strftime(", %Y")
	starttxt = dt_start.strftime("%I:%M%p").replace('AM','am').replace('PM','pm').lstrip('0')
	endtxt = dt_end.strftime("%I:%M%p").replace('AM','am').replace('PM','pm').lstrip('0')

	plaintext = \
'''From do.not.reply@engr.orst.edu  Mon Mar  9 00:21:12 2015
Return-Path: <do.not.reply@engr.orst.edu>
Received: from flip3.engr.oregonstate.edu (flip3.engr.oregonstate.edu [128.193.54.10])
	by zen.engr.oregonstate.edu (8.14.4/8.14.4) with ESMTP id t297LBLH011881;
	Mon, 9 Mar 2015 00:21:12 -0700
Date: Mon, 9 Mar 2015 00:21:11 -0700
Message-Id: <201503090721.t297LBLH011881@zen.engr.oregonstate.edu>
Content-Type: text/plain; charset="us-ascii"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
From: do.not.reply@engr.orst.edu
To: %s, %s
Cc: 
Subject: Advising Signup with %s confirmed for %s


	Advising Signup with %s confirmed
	Name: %s
	Email: %s
	Date: %s
	Time: %s - %s


	Please contact support@engr.oregonstate.edu if you experience problems
	
''' % (stud_email, adv_email, advisor, student, advisor, student, stud_email,
	datetxt, starttxt, endtxt)

	return plaintext

def get_plaintext_drop_appt(advisor='Advisor Chuaprasert, Rittie', 
	adv_email='chuaprar@engr.orst.edu', 
	student='Student Rix, Jeffrey Allan',
	stud_email='rixempire@gmail.com',
	dt_start=datetime(2015,3,10,12,30),
	dt_end=datetime(2015,3,10,13,45)):

	# prepare for date and time signatures	
	datesuffix = get_date_suffix(int(dt_start.strftime("%d")))
	datetxt = dt_start.strftime("%A, %B %d") + datesuffix + dt_start.strftime(", %Y")
	starttxt = dt_start.strftime("%I:%M%p").replace('AM','am').replace('PM','pm')
	endtxt = dt_end.strftime("%I:%M%p").replace('AM','am').replace('PM','pm')

	plaintext = \
'''From do.not.reply@engr.orst.edu  Mon Mar  9 00:24:09 2015
Return-Path: <do.not.reply@engr.orst.edu>
Received: from flip3.engr.oregonstate.edu (flip3.engr.oregonstate.edu [128.193.54.10])
	by zen.engr.oregonstate.edu (8.14.4/8.14.4) with ESMTP id t297O9Ps012644;
	Mon, 9 Mar 2015 00:24:09 -0700
Date: Mon, 9 Mar 2015 00:24:09 -0700
Message-Id: <201503090724.t297O9Ps012644@zen.engr.oregonstate.edu>
Content-Type: text/plain; charset="us-ascii"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
From: do.not.reply@engr.orst.edu
To: %s, %s
Cc: 
Subject: Advising Signup Cancellation


	Advising Signup with %s CANCELLED
	Name: %s
	Email: %s
	Date: %s
	Time: %s - %s


	Please contact support@engr.oregonstate.edu if you experience problems
	
''' % (stud_email, adv_email, advisor, student, stud_email,
	datetxt, starttxt, endtxt)

	return plaintext

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

