'''
cli_tests.py
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
import send_conf_email
import drop_calendar, send_conf_email
import mysql.connector
import curses.panel 
import unittest
import cursescli
import random
 
from mysql.connector import errorcode

class TestSequenceFunctions(unittest.TestCase):
    
    def test_display_appoints_func(self):       
        cnx = cursescli.create_db_connection()         
        
        try:
            for x in range(0, 1000):
                data1 =  cursescli.get_appointments_list(cnx)    
                # print str(data1[0])
                data = [data1[0]]
               
                for x in range(0, random.randint(0, 10)):
                    data.append(data[0])
                    
                y =  random.randint(1, 100)
                count = len(data)
                appt_selected = random.randint(0, y * 2)
                print 'y ' + str(y) + ' count ' + str(count) + ' appt selecte ' + str(appt_selected)  + ' data length' + str(len(data))              
               
                stdscr = curses.initscr()
                curses.noecho()
                curses.cbreak()
                stdscr.keypad(1)
                stdscr.scrollok(1)

                if appt_selected == 0:
                    self.assertEqual(cursescli.display_appointments(stdscr, data, y, appt_selected), 1)
                elif appt_selected > count:
                    self.assertEqual(cursescli.display_appointments(stdscr, data, y, appt_selected), count)
                else:                
                    self.assertEqual(cursescli.display_appointments(stdscr, data, y, appt_selected), appt_selected)
                    
                stdscr.keypad(0)
                curses.nocbreak()
                curses.echo()
                curses.endwin()
                
                print 'pass'
        except:
            # In event of error, restore terminal to sane state.
            stdscr.keypad(0)
            curses.nocbreak()
            curses.echo()
            curses.endwin()
            traceback.print_exc()                
       
if  __name__ == "__main__":
    unittest.main()