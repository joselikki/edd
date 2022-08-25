import sys

def map_key(key:str) -> str:

    if key == "A": return "ARROW_UP"
    if key == "B": return "ARROW_DOWN"
    if key == "C": return "ARROW_RIGHT"
    if key == "D": return "ARROW_LEFT"
    if key == "5": return "PAGE_UP" 
    if key == "6": return "PAGE_DOWN"


def read_key() -> str:
    char =''
    seq = [0,0,0,0]

    while(char == ''):
        char = sys.stdin.read(1)
    
    if char == '\x1b':
        seq[0] = sys.stdin.read(1)
        seq[1] = sys.stdin.read(1)

        if(seq[0] == '[' and seq[1] != ""):
            char = map_key(seq[1])
                

    return char
