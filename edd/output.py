from buff import BufferOut
from editor import Editor

def scroll(ed: Editor):
    if ed.cy < ed.rowoff:
        ed.rowoff = ed.cy
    if ed.cy >= ed.rowoff + ed.screen_rows:
        ed.rowoff = ed.rowoff + 1

def draw_rows(ed: Editor, buff: BufferOut):
    
    for i in range(ed.screen_rows):
        filerow = i + ed.rowoff

        if filerow >= ed.num_rows:

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
            buff.add(ed.row.chars[filerow].rstrip('\n')) 

        buff.add("\x1b[K")

        if i < (ed.screen_rows - 1):
            buff.add("\r\n")
            



def refresh_screen(ed: Editor):
    buff = BufferOut()
    scroll(ed)

    buff.add("\x1b[?25l")
    buff.add("\x1b[H")

    draw_rows(ed, buff)

    buff.add(f"\x1b[{ed.cy - ed.rowoff + 1};{ed.cx + 1}H")
    buff.add("\x1b[?25h")

    print(buff.content, end="", flush=True)
    

def clean_screen():
    print("\x1b[2J", end="", flush=True)
    print("\x1b[H", end="", flush=True)
