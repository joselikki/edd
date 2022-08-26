from buff import BufferOut
from editor import Editor

def draw_rows(ed: Editor, buff: BufferOut):
    
    total_rows = ed.total_rows()
    for i in range(total_rows):
        
        if i >= ed.num_rows:

            #editor welcome message
            if(ed.num_rows == 0 and i == int(ed.screen_rows/2)):
                padding = int((ed.screen_cols - len(ed.welcome_msg))/2)
                
                if padding:
                    buff.add("~")
                    buff.add(" " * (padding - 1 ))

                buff.add(ed.welcome_msg)

            else:
                buff.add("~")

        else:
            try:
                buff.add(ed.row.chars[i].rstrip('\n')) 
            except IndexError:
                pass

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
    

def clean_screen():
    print("\x1b[2J", end="", flush=True)
    print("\x1b[H", end="", flush=True)
