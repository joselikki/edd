import os

class Row:

    def __init__(self, num: int, chars: str) -> None:
        self.number = num
        self.chars = chars

    @property
    def size(self) -> int:
        return len(self.chars)


class EditorRows:

    def __init__(self) -> None:
        self.rows = []

    def add_row(self, row: Row) -> None:
        self.rows.append(row)

    def get_row(self, index:int) -> str:

        if index <= len(self.rows):
            return self.rows[index]

class Editor:

    def __init__(self):
        self.screen_rows = os.get_terminal_size().lines - 1
        self.screen_cols = os.get_terminal_size().columns
        self.cx = 0
        self.cy = 0
        self.rowoff = 0
        self.coloff = 0
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
