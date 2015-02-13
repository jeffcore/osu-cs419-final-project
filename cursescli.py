import curses
import traceback
import datetime
import binascii
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
        "SELECT id, student_name, appointment_date,"  
        "appointment_start_time,appointment_end_time FROM appointment WHERE advisor_email = (%s)"
    )
    username = username + "@onid.oregonstate.edu"    
    cursor.execute(query, (username,))
    data = cursor.fetchall()   
    return data

def display_main_screen(cnx, stdscr, username):    
    error = False
    data = None
    while True:        
        stdscr.addstr("Welcome to Advisor Appointment CLI!\n\n")    
        if error:                
            stdscr.addstr("Error: no appointments found for user.\n")   
        else:
            stdscr.addstr("\n")
            
        if username == "":
            stdscr.addstr("Type Your OSU Username: ")            
            curses.echo()
            username = stdscr.getstr(3,24,30)                                
      
        data = get_appointments_list(cnx, username)
        rowcount = len(data)
        
        if rowcount == 0: 
            error = True
            username = ""
            stdscr.clear()
        else:
            break
    
    return data, username
    
def display_appointments(stdscr, data, appt_num, screen_x):
    # display appointments 
    x = 1
    if appt_num > 0:
        stdscr.addstr("\nAppointment " + str(appt_num) + " Has Been Deleted\n")     
    stdscr.addstr("ID\tStudent Name\t\tAppt Date\tStart Time\tEnd Time\n")  
    for row in data:            
        row_text = str(row[0]) + "\t"
        row_text += row[1] + "\t"
        row_text += str(row[2]) + "\t"
        row_text += str(row[3]) + "\t"
        row_text += str(row[4])
        if x <= screen_x:
            stdscr.addstr(row_text + "\n")    
        x += 1
    
    # if len(data) > (appt_page_number  * appt_per_page):
    #    stdscr.addstr("       See More Results - Press UP or DOWN Arro") 
        
    
def get_appointment_number(stdscr, line_start_action_input):   
    #get action from user
    stdscr.addstr(line_start_action_input,0, "\nDelete Appointment - Enter Number (or 'q' to quit)\n")   
    input = ""
    quit = False
    cursor_location = 0
    while True:
        event = stdscr.getch(line_start_action_input+2,cursor_location)
        # stdscr.addstr(str(event))    
        if event == ord("q"): 
            quit = True
            break
        elif ord("0") <= event <= ord("9"):
            input += chr(event)   
            cursor_location+=1           
        elif event == 10:
            break           
        elif event == curses.KEY_DOWN:            
            break            
        elif event == curses.KEY_UP:
            break  
        elif event == 10:
            break           
        else:
            None   
    return input, quit
    
def main():
    cnx = create_db_connection()
    username = ""
    appt_num = 0
    appt_per_page = 10
    appt_page_number = 1
    try:
        #initialize curses
        stdscr = curses.initscr()
        scrsize = stdscr.getmaxyx()
        linesused = 7
        lines_for_appt_display = scrsize[0] - linesused
        line_start_action_input = scrsize[0] - 3
        #Turn off echoing of keys
        #enter cbreak mode
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(1)
        stdscr.scrollok(1)
                
        while True:
            stdscr.clear()
            # load top of screen includes username search
            data, username = display_main_screen(cnx, stdscr, username)
                        
            # display appointments         
            display_appointments(stdscr, data, appt_num, lines_for_appt_display)            
                
            while True:        
                input, quit = get_appointment_number(stdscr, line_start_action_input)          
            
                if not quit:
                    stdscr.addstr(input)    
                                
                    try:
                        appt_num = int(input)
                        
                        match = False
                        for row in data:  
                            if row[0] == appt_num:
                                match = True
                        
                        if match:
                            # stdscr.addstr("\nAppointment " + str(appt_num) + " Has Been Deleted\n")                             
                            break
                        else:
                            stdscr.deleteln()
                            stdscr.addstr(line_start_action_input+2, 10, "Appointment " + str(appt_num) + " Does Not Exist")    
                    except:
                        stdscr.deleteln()
                        stdscr.addstr(line_start_action_input+2, 10, "Invalid number")  
                else:
                    break
        
            if quit:
                break        
            
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