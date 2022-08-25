import sys
import os
from editor import Editor
from terminal import Terminal, editor_read_key
from output import clean_screen, refresh_screen, draw_rows

term = Terminal()

ed = Editor()
ed.rows = os.get_terminal_size().lines
ed.cols = os.get_terminal_size().columns

def ctrl_key(key: str) -> int:
    try:
        key_num = ord(key) & 0x1f
        return key_num
    except:
        return 0

def editor_process_keypress():
    char = editor_read_key()

    if ord(char) == ctrl_key('q'):
        clean_screen()
        exit(0)

def main():
    term.enable_raw_mode()
    
    while(True):
        refresh_screen(ed)
        editor_process_keypress()


if __name__ == '__main__':
    try:
        main()
    finally:
        term.disable_raw_mode()
