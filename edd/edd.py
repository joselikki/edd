import sys
from editor import Editor
from terminal import Terminal
from screen import clean_screen, refresh_screen
from control import handle_keypress


def main():

    terminal = Terminal()
    editor = Editor()

    try:
        terminal.enable_raw_mode()

        if (len(sys.argv)> 1):
            editor.open_file(sys.argv[1])

        while(True):
            refresh_screen(editor)
            handle_keypress(editor)

    finally:
        clean_screen()
        terminal.disable_raw_mode()

if __name__ == '__main__':
        main()
