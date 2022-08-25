import os
from editor import Editor
from terminal import Terminal 
from output import clean_screen, refresh_screen
from key import read_key

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


def move_cursor(ed: Editor, key: str):
    
    if key == "ARROW_LEFT":
        ed.cx -= 1
    
    elif key == "ARROW_RIGHT":
        ed.cx += 1

    elif key == "ARROW_UP":
        ed.cy -= 1
    
    elif key == "ARROW_DOWN":
        ed.cy += 1
    
    else:
        return

def editor_process_keypress():
    char = read_key()
    mov_keys = ["ARROW_UP", "ARROW_DOWN", "ARROW_RIGHT", "ARROW_LEFT"]

    try:
        if ord(char) == ctrl_key('q'):
            clean_screen()
            exit(0)

    except TypeError:
        if char in mov_keys:
            move_cursor(ed, char)


def main():
    term.enable_raw_mode()
    
    while(True):
        refresh_screen(ed)
        editor_process_keypress()


if __name__ == '__main__':
    try:
        main()
    finally:
        clean_screen()
        term.disable_raw_mode()
