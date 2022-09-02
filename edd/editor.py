import os

class EditorRow:

    def __init__(self):
        self.size = 0
        self.chars = []
        
class Editor:
    
    def __init__(self):
        self.screen_rows = os.get_terminal_size().lines - 1
        self.screen_cols = os.get_terminal_size().columns 
        self.cx = 0
        self.cy = 0
        self.rowoff = 0
        self.num_rows = 0 
        self.rows = EditorRow() 
        self.welcome_msg = "EDD VERSION 0.0.1"
        self.filename = "[NEW FILE]"

    def open_file(self, filename:str):
        self.filename = filename

        f = open(filename, "r")
        lines = f.readlines()
        self.rows.chars = lines
        self.num_rows = len(lines)
        f.close()

