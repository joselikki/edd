from buff import BufferOut
from editor import Editor


def scroll(editor: Editor):

    if editor.cy < editor.rowoff:
        editor.rowoff = editor.cy

    if editor.cy >= editor.rowoff + editor.screen_rows:
        editor.rowoff = editor.cy - editor.screen_rows + 1


def draw_rows(editor: Editor, buff: BufferOut):
    
    for i in range(editor.screen_rows):
        filerow = i + editor.rowoff

        if filerow >= editor.num_rows:

            #editor welcome message
            if(editor.num_rows == 0 and i == int(editor.screen_rows/2)):
                padding = int((editor.screen_cols - len(editor.welcome_msg))/2)
                
                if padding:
                    buff.add("~")
                    buff.add(" " * (padding - 1 ))

                buff.add(editor.welcome_msg)

            else:
                buff.add("~")

        else:
            buff.add(editor.row.chars[filerow].rstrip('\n')) 

        buff.add("\x1b[K")

        if i < (editor.screen_rows - 1):
            buff.add("\r\n")
            

def refresh_screen(editor: Editor):
    buff = BufferOut()
    scroll(editor)

    buff.add("\x1b[?25l")
    buff.add("\x1b[H")

    draw_rows(editor, buff)

    buff.add(f"\x1b[{editor.cy - editor.rowoff + 1};{editor.cx + 1}H")
    buff.add("\x1b[?25h")

    print(buff.content, end="", flush=True)
    

def clean_screen():
    print("\x1b[2J", end="", flush=True)
    print("\x1b[H", end="", flush=True)
