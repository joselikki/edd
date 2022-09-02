from editor import Editor
from buffer import Buffer

def statusbar(editor: Editor, buffer: Buffer):
    
    buffer.add("\x1b[7m")
    bar_len = len(editor.filename)
    
    buffer.add(editor.filename)
    while (bar_len < editor.screen_cols):
        msg = f"{editor.cy + 1},{editor.cx + 1}"

        if bar_len == int(editor.screen_cols / 2) - len(msg):
            buffer.add(msg)
            bar_len += len(msg)

        else:
            buffer.add(" ")
            bar_len += 1

    buffer.add("\x1b[m")
