import sys
from editor import Editor
from terminal import Terminal 
from output import clean_screen, refresh_screen
from control import handle_keypress


def editor_open(editor: Editor, filename:str):
    editor.filename = filename
    f = open(filename, "r")
    lines = f.readlines()

    editor.row.size = len(lines)
    editor.row.chars = lines
    editor.num_rows = len(lines) 
    f.close()

def main():
    

    terminal = Terminal()
    editor = Editor()

    try:
        terminal.enable_raw_mode()

        if (len(sys.argv)> 1):
            editor_open(editor, sys.argv[1])

        while(True):
            refresh_screen(editor)
            handle_keypress(editor)

    finally:
        clean_screen()
        terminal.disable_raw_mode()

if __name__ == '__main__':
        main()
