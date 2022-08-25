import sys
import os
from terminal import enable_raw_mode, disable_raw_mode, editor_read_key

COLS = os.get_terminal_size().columns
ROWS = os.get_terminal_size().lines

class BufferOut:

    def __init__(self):
       self.content = ''

    def add(self, chars : str):
        self.content = self.content + chars



def ctrl_key(key: str) -> int:
    try:
        key_num = ord(key) & 0x1f
        return key_num
    except:
        return 0

def clean_screen():
    print("\x1b[2J", end="", flush=True)
    print("\x1b[H", end="", flush=True)

def editor_process_keypress():
    char = editor_read_key()

    if ord(char) == ctrl_key('q'):
        clean_screen()
        exit(0)


def draw_rows(buff: BufferOut):
    for i in range(ROWS):
        buff.add("~")
        buff.add("\x1b[K")

        if i < (ROWS - 1):
            buff.add("\r\n")

def editor_refresh_screen():
    buff = BufferOut()
    
    buff.add("\x1b[?25l")
    buff.add("\x1b[H")

    draw_rows(buff)

    buff.add("\x1b[H")
    buff.add("\x1b[?25h")

    print(buff.content, end="", flush=True)
    

def main():
    enable_raw_mode()
    
    while(True):
        editor_refresh_screen()
        editor_process_keypress()


if __name__ == '__main__':
    try:
        main()
    finally:
        disable_raw_mode()
