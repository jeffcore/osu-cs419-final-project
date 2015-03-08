'''
cursescli.py
This module contains the curses CLI application for the CS419 Project
Simplifed Advising Scheduling for our implementation.
'''
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
import curses.panel 
from mysql.connector import errorcode

def verify_deletion(stdscr):
    window = curses.newwin(3,20,4,4)
    window.addstr(0, 0, "Hello, world!")
    panel1 = curses.panel.new_panel(window)
    
    curses.panel.update_panels()
    stdscr.refresh()
    
    panel1.top(); 
    curses.panel.update_panels() 
    stdscr.refresh() 
    window.getch()
   
    return
    
    
        
def main():
   
    try:
        #initialize curses
        stdscr = curses.initscr()
        scrsize = stdscr.getmaxyx()
        lines_used_not_for_appt = 7
        lines_used_for_action_input = 3
        lines_for_appt_display = scrsize[0] - lines_used_not_for_appt   # number of total rows - non appt rows
        line_start_action_input = scrsize[0] - lines_used_for_action_input  #row number to start displaying input section
        #Turn off echoing of keys
        # enter cbreak mode
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(1)
        stdscr.scrollok(1)
        
       
        verify_deletion(stdscr)
        
        
        # clean up screen and return to normal command line 
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