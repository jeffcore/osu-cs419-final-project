import curses
import mysql.connector
from mysql.connector import errorcode

def main():
    # try:    
    # cnx = mysql.connector.connect(user='scott', password='tiger', host='127.0.0.1', database='employees')
    # except mysql.connector.Error as err:
    stdscr = curses.initscr()

    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1)

    stdscr.addstr("Welcome to Advisor Appointment CLI!\n\n")
  
    while True:
        event = stdscr.getch()
        if event == ord("q"): break

    stdscr.keypad(0)
    curses.nocbreak()
    curses.echo()

    curses.endwin()



if  __name__ == "__main__":
    main()

