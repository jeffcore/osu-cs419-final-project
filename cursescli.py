import curses
import traceback
import datetime
import mysql.connector
from mysql.connector import errorcode


def create_db_connection():
    db_user = "cs419-g8"
    db_password = "9bWxwfvCAqUncYZV"
    db_host = "mysql.eecs.oregonstate.edu"
    db_database="cs419-g8"

    try:
        cnx = mysql.connector.connect(user=db_user, password=db_password, host=db_host, database=db_database)        
    except mysql.connector.Error as err:
        print "DB Connection Error"
		

    return cnx


def get_appointments_list(cnx, username):
    cursor = cnx.cursor()
    query = (
        "SELECT id, student_name, student_email, appointment_date,"  
        "appointment_start_time,appointment_end_time FROM appointment WHERE advisor_email = (%s)"
    )
    username = username + "@onid.oregonstate.edu"    
    cursor.execute(query, (username,))
    data = cursor.fetchall()   
    return data



def main():
    cnx = create_db_connection()
    f = '%Y-%m-%d'
     
    try:
        #initialize curses
        stdscr = curses.initscr()
        #Turn off echoing of keys
        #enter cbreak mode
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(1)
        
        # get username
        error = False        
        while True:        
            stdscr.addstr("Welcome to Advisor Appointment CLI!\n\n")    
            if error:                
                stdscr.addstr("Error: no appointments for user.\n")   
            else:
                stdscr.addstr("\n")
                
            stdscr.addstr("Type Your OSU Username: ")            
            curses.echo()
            username = stdscr.getstr(3,24,30)                    
            data = get_appointments_list(cnx, username)
            if len(data) == 0: 
                error = True
                stdscr.clear()
            else:
                break
        
        # display appointments         
        stdscr.addstr("ID\tStudent Name\t\tStudent Email\t\t\tAppt Date\tStart Time\tEnd Time\n")  
        for row in data:            
            row_text = str(row[0]) + "\t"
            row_text = row_text + row[1] + "\t"
            row_text = row_text + row[2] + "\t"
            # row_text = row_text + str(datetime.datetime.strptime(row[3], f))            
            row_text = row_text + str(row[3]) + "\t"
            row_text = row_text + str(row[4]) + "\t"
            row_text = row_text + str(row[5])
            stdscr.addstr(row_text + "\n")   
        
        #get action from user
        stdscr.addstr("\nDelete Appointment - Enter Number (or 'q' to quit)\n")   
        while True:
            event = stdscr.getch()
            if event == ord("q"): 
                break
            else:
                stdscr.addstr("\nAppointment " + str(int(event))+ " Has Been Deleted\n")   
            

        stdscr.keypad(0)
        curses.nocbreak()
        curses.echo()

        curses.endwin()
    except:
        # In event of error, restore terminal to sane state.
        stdscr.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        traceback.print_exc()           # Print the exception


if  __name__ == "__main__":
    main()