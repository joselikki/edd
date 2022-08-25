import os

class Editor:
    
    def __init__(self):
        self.rows = os.get_terminal_size().lines
        self.cols = os.get_terminal_size().columns
        self.cx = 0
        self.cy = 0
    
