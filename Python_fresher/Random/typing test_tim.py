import curses
from curses import wrapper
import time
import random

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("welcome to typing speed test")
    stdscr.addstr("\npress any key to continue")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, user, wpm=0):
     #target text needs to be defined in display_text function to use in the next line
    stdscr.addstr(target)
    stdscr.addstr(1,0, f"WPM:{wpm}")

    for i, char in enumerate(user):
        correct_char=target[i]
        color=curses.color_pair(2)
        if char!=correct_char:
            color=curses.color_pair(3)
        stdscr.addstr(0, i, char, color)

def load_text():
    with open("target_text.txt", "r") as f:
        lines=f.readlines()
        #if not used strip() here, usertext and target text len will not match at line 45
        return random.choice(lines).strip()


def wpm_test(stdscr):
    target_text = load_text()
    user_text = []
    wpm=0
    start_time=time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed=max(time.time()-start_time, 1)
        wpm=round((len(user_text)/(time_elapsed/60))/5)
        stdscr.clear()
        display_text(stdscr, target_text, user_text, wpm)
        stdscr.refresh()

        if len("".join(user_text))==len(target_text):
            stdscr.nodelay(False)
            break

        try:
            key=stdscr.getkey()
        except:
            continue
        
        if ord(key)==27:
            break

        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(user_text)>0:
                user_text.pop()
        elif len(user_text)<len(target_text):
            user_text.append(key)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)

        stdscr.addstr(2,0, "you have completed the test. press any key to continue")
        key=stdscr.getkey()
        if ord(key)==27:
            break


wrapper(main)

