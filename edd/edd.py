from editor import Editor
from terminal import Terminal 
from output import clean_screen, refresh_screen
from control import handle_keypress


def main():
    term = Terminal()
    edd = Editor()

    try:

        term.enable_raw_mode()
        
        while(True):
            refresh_screen(edd)
            handle_keypress(edd)

    finally:
        clean_screen()
        term.disable_raw_mode()

if __name__ == '__main__':
        main()
