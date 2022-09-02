from editor import Editor
from key import read_key


def ctrl_key(key: str) -> int:
    try:
        key_num = ord(key) & 0x1f
        return key_num
    except:
        return 0



def move_cursor(editor: Editor, key: str):

    if key == "ARROW_LEFT" and editor.cx != 0:
        editor.cx -= 1
    
    elif key == "ARROW_RIGHT" and editor.cx != editor.screen_cols - 1:
        editor.cx += 1

    elif key == "ARROW_UP" and editor.cy != 0:
        editor.cy -= 1
    
    elif key == "ARROW_DOWN" and editor.cy < editor.num_rows :
        editor.cy += 1
    
    else:
        return  

def handle_keypress(editor: Editor):
    char = read_key()
    mov_keys = [
                "ARROW_UP", 
                "ARROW_DOWN", 
                "ARROW_RIGHT", 
                "ARROW_LEFT"
                ]

    try:
        if ord(char) == ctrl_key('q'):
            exit(0)

    except TypeError:
        if char in mov_keys:
            move_cursor(editor, char)


