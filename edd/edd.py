import sys
from editor import Editor
from terminal import Terminal 
from output import clean_screen, refresh_screen
from control import handle_keypress


def editor_open(ed: Editor, filename:str):
    f = open(filename, "r")
    line = f.readline()

    ed.row.size = len(line)
    ed.row.chars = line.strip()
    ed.num_rows = 1 
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
