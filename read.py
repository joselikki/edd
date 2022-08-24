import sys
import termios

STDIN_FD = sys.stdin.fileno()
ORIG_TERMIOS = termios.tcgetattr(STDIN_FD)

def ctrl_key(key: str) -> int:
    try:
        key_num = ord(key) & 0x1f
        return key_num
    except:
        return 0

def disable_raw_mode():
    termios.tcsetattr(STDIN_FD, termios.TCSAFLUSH, ORIG_TERMIOS)

def enable_raw_mode():

    raw_termios = ORIG_TERMIOS.copy()
    raw_termios[0] &= ~(termios.BRKINT | termios.ICRNL | termios.INPCK | termios.ISTRIP | termios.IXON)
    raw_termios[1] &= ~(termios.OPOST)
    raw_termios[3] &= ~(termios.ECHO | termios.ICANON | termios.IEXTEN | termios.ISIG)
    raw_termios[6][termios.VMIN] = 0
    raw_termios[6][termios.VTIME] = 1

    termios.tcsetattr(sys.stdin.fileno(), termios.TCSAFLUSH, raw_termios)


def main():
    enable_raw_mode()
    
    while(True):
        
        try:        
            char = sys.stdin.read(1)
            if(ord(char) == ctrl_key("q")):
                break

            print(char, "\r\n", end="")    
        except:
            print(0, "\r\n", end="")

if __name__ == '__main__':
    try:
        main()
    finally:
        disable_raw_mode()
