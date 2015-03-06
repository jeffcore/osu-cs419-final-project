import curses
import traceback
import datetime
import binascii
import sql_cmd
import db_funcs
import procfilter
import datetime
import drop_appt
import drop_calendar, send_conf_email
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
        "SELECT id, student_name, appointment_date,appointment_start_time,appointment_end_time,"  
        "advisor_name, advisor_email, student_email FROM temp WHERE advisor_email = (%s)"
    )
 
    cursor.execute(query, (username,))
    data = cursor.fetchall()   
    
    cnx.commit()
    cursor.close()
    
    
    f = open('data.txt', 'a')
    f.write(str(data)) 
    f.close()
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
        username =  'chuaprar@engr.orst.edu' #delete line
        
        if username == "":
            stdscr.addstr("Type In Your OSU email: ")            
            curses.echo()
            username = stdscr.getstr(3,24,30)                                
      
        data = get_appointments_list(cnx, 'chuaprar@engr.orst.edu') # and username variable here
        rowcount = len(data)
        
        if rowcount == 0: 
            error = True
            username = ""
            stdscr.clear()
        else:
            break
    
    return data, username

   # rixj@onid.oregonstate.edu
def display_appointments(stdscr, data, appt_num, screen_x, appt_selected):
    # display appointments 
    # set highlight and normal colors
    curses.start_color()
    curses.init_pair(1,curses.COLOR_RED, curses.COLOR_WHITE)
    h = curses.color_pair(1)
    n = curses.A_NORMAL

    x = 1
    
    if appt_num > 0:
        stdscr.addstr("\nAppointment " + str(appt_num) + " Has Been Deleted\n")     
    stdscr.addstr("ID\tStudent Name\t\tAppt Date\tStart Time\tEnd Time\n")  
    for row in data:            
        row_text = str(row[0]) + "\t"   # appoint id
        row_text += row[1] + "\t"       # student name
        row_text += str(row[2]) + "\t"  # appointment date
        row_text += str(row[3]) + " \t"  # appointment start time
        row_text += str(row[4])         # appointment end time
        if x <= screen_x:
            if x == appt_selected:
                stdscr.addstr(row_text + "\n", h)   
            else:
                stdscr.addstr(row_text + "\n", n) 
        x += 1
    
    # if len(data) > (appt_page_number  * appt_per_page):
    #    stdscr.addstr("       See More Results - Press UP or DOWN Arro") 
        
    return
    
def get_appointment_number(stdscr, line_start_action_input, appt_selected):   
    #get action from user
    stdscr.addstr(line_start_action_input,0, "\nUp/Down Arrow to Select | d to Delete | q to Quit  | r to Refresh")   
    input = ""
    quit = False
    cursor_location = 0
    while True:
        event = stdscr.getch(line_start_action_input+2,cursor_location)
        # stdscr.addstr(str(event))    
        if event == ord("q"): 
            input = chr(event)  
            quit = True
            break
        elif event == ord("d"): 
            input = chr(event)  
            break            
        elif event == ord("r"): 
            input = chr(event)  
            break            
        elif event == 10:
            break           
        elif event == curses.KEY_DOWN:            
            appt_selected += 1  
            break              
        elif event == curses.KEY_UP:
            appt_selected -= 1
            break  
    return input, appt_selected, quit
    
def handle_drop(appointment):      
    # extract necessary data from appointment array
    db_uid = appointment[0]
    db_adv = appointment[5]
    db_adv_email = appointment[6]
    db_date = str(appointment[2])
    db_start = str(appointment[3])
    db_end = str(appointment[4])
    db_stud = appointment[1]
    db_stud_email = appointment[7]
    
    # create unique id
    uid = db_adv_email + '::' + db_date + '::' + db_start  
    
    # prepare datetime info
    dt_start = datetime.datetime.strptime(db_date + ' ' + db_start, '%Y-%m-%d %H:%M:%S')
    dt_end = datetime.datetime.strptime(db_date + ' ' + db_end, '%Y-%m-%d %H:%M:%S')
        
    # send Outlook calendar invite to advisor    
    #drop_appt.main(db_adv, db_adv_email, dt_start, dt_end)
    drop_calendar.drop_calendar(db_adv, db_stud, db_adv_email, dt_start, dt_end, uid)
    db_funcs.drop_appt_by_id(db_uid)
      
    return
        
def main():
    cnx = create_db_connection()
    username = ""
    appt_num = 0
    appt_per_page = 10
    appt_page_number = 1
    appt_selected = 1
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
            data = None
            data, username = display_main_screen(cnx, stdscr, username)
          
            if appt_selected < 1:
                appt_selected = 1    
            elif appt_selected > len(data):
                appt_selected -= 1
                
            # display appointments         
            display_appointments(stdscr, data, appt_num, lines_for_appt_display, appt_selected)                       
            stdscr.refresh();            
            input, appt_selected, quit = get_appointment_number(stdscr, line_start_action_input, appt_selected)       
          
            if not quit:
                stdscr.addstr(input)    
                
                if input == "d" or input == 'd':
                    try:                                                           
                        appointment = data[appt_selected-1]                        
                        appt_num = int(appointment[0])                                
                        handle_drop(appointment)
                        # data.remove(appt_selected-1)                        
                    except Exception as inst:                                             
                        f = open('error.txt', 'w')
                        f.write(str(inst)) 
                        f.close()
                        stdscr.deleteln()
                        stdscr.addstr(line_start_action_input+2, 10, "Invalid number")  
                
            else:
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