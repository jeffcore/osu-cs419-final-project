import curses
import locale
import os
import shlex
import signal
import sys

def curse_mode(scr):
    curses.noecho()
    curses.cbreak()
    scr.keypad(1)

def uncurse_mode(scr):
    curses.echo()
    curses.nocbreak()
    scr.keypad(0)

def launch_work(scr, el, worker):
    # screen in normal mode
    scr.clear()
    scr.refresh()
    scr.move(0,0)
    uncurse_mode(scr)

    ret = worker(el)

    # back to curse mode
    curse_mode(scr)
    return ret == 0

def blank_screen(scr):
    cap_y,cap_x = list(scr.getmaxyx())
    for y in range(cap_y):
        scr.addstr(y, 0, ''.join([ " " for k in range(cap_x-1)]))

def disp_title(scr, title):
    _,cap_x = scr.getmaxyx()
    y,_ = scr.getyx()
    if len(title) >= cap_x:
        title = title[:cap_x-1]
    scr.addstr(y,0,title)
    scr.addstr(y+1,0,''.join([ '-' for k in range(len(title)) ]))
    scr.move(y+2, 0)

def disp_choices(scr, els, sel):
    _,cap_x = scr.getmaxyx()
    y,_ = scr.getyx()
    for k,c in enumerate(els):
        if len(c) >= cap_x:
            c = c[:cap_x-1]

        if k == sel:
            mode = curses.A_STANDOUT
        else:
            mode = curses.A_NORMAL
        scr.addstr(y, 0, c, mode)
        y += 1

def comp_scroll(scr, selected, fst_disp):
    y,x = scr.getyx()
    cap_y,_ = scr.getmaxyx()
    n_disps = cap_y - y
    lst_disp = fst_disp + n_disps - 1

    if selected < fst_disp:
        fst_disp = selected
        lst_disp = fst_disp + n_disps - 1
    elif selected > lst_disp:
        fst_disp = selected - n_disps + 1
        lst_disp = selected

    return fst_disp,lst_disp

def curse_engine(scr, title, els, worker):
    # encoding
    locale.setlocale(locale.LC_ALL, '')
    code = locale.getpreferredencoding()

    curses.use_default_colors()
    curses.curs_set(0)

    first_disp = 0
    selected = 0

    while True:
        cap_y,_ = list(scr.getmaxyx())
        if cap_y < 3:
            scr.refresh()
            continue

        blank_screen(scr)
        scr.move(0,0)
        # popup title
        disp_title(scr, title)

        # popup content
        first_disp, last_disp = comp_scroll(scr, selected, first_disp)
        disp_width = last_disp - first_disp + 1
        disp_choices(scr, els[first_disp:last_disp+1],
                selected - first_disp)

        scr.refresh()
        p_key = scr.getch()
        if p_key == curses.KEY_UP or p_key == ord('k'):
            selected = max(0, selected - 1)
        elif p_key == curses.KEY_DOWN or p_key == ord('j'):
            selected = min(len(els)-1, selected + 1)
        elif p_key == curses.KEY_PPAGE:
            shift = disp_width//2
            selected = max(0, selected - shift)
            first_disp = max(0, first_disp - shift)
        elif p_key == curses.KEY_NPAGE:
            shift = disp_width//2
            selected = min(len(els)-1, selected + shift)
            first_disp = min(max(0,len(els)-disp_width), first_disp + shift)
        elif p_key == curses.KEY_HOME:
            selected = 0
        elif p_key == curses.KEY_END:
            selected = len(els)-1
        elif p_key == ord('q'):
            return 0
        elif p_key == ord('\n'):
            if launch_work(scr, els[selected], worker):
                return 0
            else:
                scr.getch()
                scr.clear()

def sigint_handler(signal, frame):
    sys.exit(0)

# ----

def exec_in_term(app, term_cmd):
    self_invoc = shlex.split("python3 {0} -go".format(app))

    term_i = shlex.split(term_cmd)
    cmd = term_i[0]
    args = term_i + ["-e"] + self_invoc
    os.execve(cmd, args, os.environ)

def popup(argv, title, els, worker):
    signal.signal(signal.SIGINT, sigint_handler)
    curses.wrapper(curse_engine, title, els, worker)
