#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Shutdown/Reboot/Suspend dialog
'''

import os
import os.path
import subprocess
import sys

import ncpop

app_title = "What to do ?"
term_name = "/usr/bin/urxvt -geometry 15x6 -title halter -name halter"
systemctl_path = "/usr/bin/systemctl"

def cmd_handler(cmd):
    if cmd == 'Shutdown':
        inst = 'poweroff'
    elif cmd == 'Reboot':
        inst = 'reboot'
    elif cmd == 'Suspend':
        inst = 'suspend'
    elif cmd == 'Hibernate':
        inst = 'hibernate'
    else:
        return 1

    return 

def main():
   
    cmds = [ 'Suspend', 'Hibernate', 'Reboot', 'Shutdown' ]

    ncpop.popup(sys.argv, "the title", cmds, cmd_handler)

if __name__ == "__main__":
    sys.exit(main())
