from editor import Editor
from buff import BufferOut

def statusbar(editor: Editor, buf: BufferOut):
    
    buf.add("\x1b[7m")
    bar_len = len(editor.filename)
    
    buf.add(editor.filename)
    while (bar_len < editor.screen_cols):
        msg = f"{editor.cy + 1},{editor.cx + 1}"

        if bar_len == int(editor.screen_cols / 2) - len(msg):
            buf.add(msg)
            bar_len += len(msg)

        else:
            buf.add(" ")
            bar_len += 1

    buf.add("\x1b[m")
