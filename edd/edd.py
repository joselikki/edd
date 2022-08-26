import sys
from editor import Editor
from terminal import Terminal 
from output import clean_screen, refresh_screen
from control import handle_keypress


def editor_open(ed: Editor, filename:str):
    f = open(filename, "r")
    lines = f.readlines()

    ed.row.size = len(lines)
    ed.row.chars = lines
    ed.num_rows = len(lines) 
    f.close()

def main():
    

    term = Terminal()
    edd = Editor()

    try:
        term.enable_raw_mode()

        if (len(sys.argv)> 1):
            editor_open(edd, sys.argv[1])

        while(True):
            refresh_screen(edd)
            handle_keypress(edd)

    finally:
        clean_screen()
        term.disable_raw_mode()

if __name__ == '__main__':
        main()
