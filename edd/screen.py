from buffer import Buffer
from editor import Editor
from statusbar import statusbar


def scroll(editor: Editor):

    if editor.cy < editor.rowoff:
        editor.rowoff = editor.cy

    if editor.cy >= editor.rowoff + editor.screen_rows:
        editor.rowoff = editor.cy - editor.screen_rows + 1


def show_default_msg(cols: int, msg: str, buffer: Buffer) -> None:
    
    padding = int((cols - len(msg))/2)
    
    if padding:
        buffer.add("~")
        buffer.add(" " * (padding - 1 ))

    buffer.add(msg)



def render_rows(editor: Editor, buffer: Buffer):
    
    for i in range(editor.screen_rows):
        filerow = i + editor.rowoff

        if filerow >= editor.num_rows:

            if(editor.num_rows == 0 and i == int(editor.screen_rows/2)):
                show_default_msg(editor.screen_cols, editor.welcome_msg, buffer)

            else:
                buffer.add("~")

        else:
            row = editor.rows.get_row(filerow)
            buffer.add( row.rstrip('\n') ) 


        buffer.add("\x1b[K")
        buffer.add("\r\n")
            

def refresh_screen(editor: Editor):
    buffer = Buffer()
    scroll(editor)

    buffer.add("\x1b[?25l")
    buffer.add("\x1b[H")

    render_rows(editor, buffer)
    statusbar(editor.screen_cols, editor.filename, editor.cy, editor.cx,  buffer)
    
    buffer.add(f"\x1b[{editor.cy - editor.rowoff + 1};{editor.cx + 1}H")
    buffer.add("\x1b[?25h")

    print(buffer.content, end="", flush=True)
    

def clean_screen():
    print("\x1b[2J", end="", flush=True)
    print("\x1b[H", end="", flush=True)
