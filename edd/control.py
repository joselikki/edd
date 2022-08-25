from editor import Editor
from output import clean_screen
from key import read_key


def ctrl_key(key: str) -> int:
    try:
        key_num = ord(key) & 0x1f
        return key_num
    except:
        return 0



def move_cursor(ed: Editor, key: str):
    
    if key == "ARROW_LEFT" and ed.cx != 0:
        ed.cx -= 1
    
    elif key == "ARROW_RIGHT" and ed.cx != ed.cols - 1:
        ed.cx += 1

    elif key == "ARROW_UP" and ed.cy != 0:
        ed.cy -= 1
    
    elif key == "ARROW_DOWN" and ed.cy != ed.rows - 1:
        ed.cy += 1
    
    else:
        return  

def handle_keypress(ed: Editor):
    char = read_key()
    mov_keys = ["ARROW_UP", "ARROW_DOWN", "ARROW_RIGHT", "ARROW_LEFT"]

    try:
        if ord(char) == ctrl_key('q'):
            clean_screen()
            exit(0)

    except TypeError:
        if char in mov_keys:
            move_cursor(ed, char)


