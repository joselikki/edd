import sys
import os
from terminal import enable_raw_mode, disable_raw_mode, editor_read_key
from output import clean_screen, refresh_screen, draw_rows


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
    enable_raw_mode()
    
    while(True):
        refresh_screen()
        editor_process_keypress()


if __name__ == '__main__':
    try:
        main()
    finally:
        disable_raw_mode()
