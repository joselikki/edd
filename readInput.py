import tty, termios
import sys

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setraw(sys.stdin.fileno())   
    ch = sys.stdin.read(3)
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == "\x1b":
        print("You pressed exit!")
    elif ch == "\x1b[A":
        print("You pressed UP key!")
    else:
        print("Character is :" + ch)

getch()
