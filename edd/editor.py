import os

class Row:
    
    def __init__(self, num: int, chars: str) -> None:
        self.number = num
        self.chars = chars
        self.size = len(self.chars)
        

class EditorRows:

    def __init__(self) -> None:
        self.size = 0
        self.rows = []

    def add_row(self, row: Row) -> None:
        self.rows.append(row)

    @property
    def chars(self) -> str:
        content = []
        
        for row in self.rows:
            content.append(row.chars)

        return content

        
class Editor:
    
    def __init__(self):
        self.screen_rows = os.get_terminal_size().lines - 1
        self.screen_cols = os.get_terminal_size().columns 
        self.cx = 0
        self.cy = 0
        self.rowoff = 0
        self.num_rows = 0 
        self.rows = EditorRows() 
        self.welcome_msg = "EDD VERSION 0.0.1"
        self.filename = "[NEW FILE]"

    def open_file(self, filename:str):
        self.filename = filename

        f = open(filename, "r")
        lines = f.readlines()
        i = 0
        for line in lines:
            r = Row(i, line)
            self.rows.add_row(r)
            i += 1

        self.num_rows = i  
        f.close()
