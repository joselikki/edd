from buff import BufferOut
from editor import Editor

def clean_screen():
    print("\x1b[2J", end="", flush=True)
    print("\x1b[H", end="", flush=True)


def draw_rows(ed: Editor, buff: BufferOut):

    for i in range(ed.screen_rows):
        
        if i >= ed.num_rows:

            if(ed.num_rows == 0 and i == int(ed.screen_rows/2)):
                wel_msg = "EDD VERSION 0.0.1"
                padding = int((ed.screen_cols - len(wel_msg))/2)
                
                if padding:
                    buff.add("~")
                    padding-= 1

                while(padding):
                     buff.add(" ")
                     padding -= 1

                buff.add(wel_msg)

            else:
                buff.add("~")

        else:
            buff.add(ed.row.chars) 

        buff.add("\x1b[K")

        if i < (ed.screen_rows - 1):
            buff.add("\r\n")
            
def refresh_screen(ed: Editor):
    buff = BufferOut()
    
    buff.add("\x1b[?25l")
    buff.add("\x1b[H")

    draw_rows(ed, buff)

    buff.add(f"\x1b[{ed.cy + 1};{ed.cx + 1}H")
    buff.add("\x1b[?25h")

    print(buff.content, end="", flush=True)
    
