import os
from buff import BufferOut

COLS = os.get_terminal_size().columns
ROWS = os.get_terminal_size().lines

def clean_screen():
    print("\x1b[2J", end="", flush=True)
    print("\x1b[H", end="", flush=True)


def draw_rows(buff: BufferOut):

    for i in range(ROWS):

        if(i == int(ROWS/2)):
            wel_msg = "EDITOR VERSION 0.0.1"
            padding = int((COLS - len(wel_msg))/2)
            
            if padding:
                buff.add("~")
                padding-= 1

            while(padding):
                 buff.add(" ")
                 padding -= 1

            buff.add(wel_msg)

        else:
            buff.add("~")

        buff.add("\x1b[K")

        if i < (ROWS - 1):
            buff.add("\r\n")
            
def refresh_screen():
    buff = BufferOut()
    
    buff.add("\x1b[?25l")
    buff.add("\x1b[H")

    draw_rows(buff)

    buff.add("\x1b[H")
    buff.add("\x1b[?25h")

    print(buff.content, end="", flush=True)
    
