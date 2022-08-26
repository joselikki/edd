import os

class EditorRow:

    def __init__(self):
        self.size = 0
        self.chars = ""

class Editor:
    
    def __init__(self):
        self.screen_rows = os.get_terminal_size().lines
        self.screen_cols = os.get_terminal_size().columns
        self.cx = 0
        self.cy = 0
        self.num_rows = 0 
        self.row = EditorRow() 
