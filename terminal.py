import sys
import termios


class Terminal:
    STDIN_FD = sys.stdin.fileno()


    def __init__(self):
        self._orig_settings = termios.tcgetattr(self.STDIN_FD)
    
    def enable_raw_mode(self):
        raw_settings = self._orig_settings.copy()
        raw_settings[0] &= ~(termios.BRKINT | termios.ICRNL | termios.INPCK | termios.ISTRIP | termios.IXON)
        raw_settings[1] &= ~(termios.OPOST)
        raw_settings[3] &= ~(termios.ECHO | termios.ICANON | termios.IEXTEN | termios.ISIG)
        raw_settings[6][termios.VMIN] = 0
        raw_settings[6][termios.VTIME] = 1

        termios.tcsetattr(self.STDIN_FD, termios.TCSAFLUSH, raw_settings)

    def disable_raw_mode(self):
        termios.tcsetattr(self.STDIN_FD, termios.TCSAFLUSH, self._orig_settings)



def editor_read_key():
    char =''
    while(char == ''):
        char = sys.stdin.read(1)

    return char
    
