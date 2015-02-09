import sys
import email

def main(argv):

	full_msg = sys.stdin.readlines()
	msg = ''.join(full_msg)

	if (msg.count('Advising Signup Cancellation') == 1):
		msg += '\nDROP'
		add = False
	else:
		msg += '\nADD'
		add = True

	f = open('CS419/CS419mail/proc_echo.txt', 'w')
	f.write(msg)
	f.close()

from db_funcs import view_appt
def runtest():
	view_appt()

if __name__ == "__main__":

	main(sys.argv[1:])
