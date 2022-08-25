import sys

def map_arrow(arrow) -> str:

    if arrow == "A": return "ARROW_UP"
    if arrow == "B": return "ARROW_DOWN"
    if arrow == "C": return "ARROW_RIGHT"
    if arrow == "D": return "ARROW_LEFT"
    


def read_key():
    char =''
    char_seq = [0,0,0,0]

    while(char == ''):
        char = sys.stdin.read(1)
    
    if char == '\x1b':
        char_seq[0] = sys.stdin.read(1)
        char_seq[1] = sys.stdin.read(1)

        if(char_seq[0] == '[' and char_seq[1] != ""):
            char = map_arrow(char_seq[1])
                

    return char
