
class Buffer:

    def __init__(self) -> None:
       self.content = ''

    def add(self, chars : str) -> None:
        self.content = self.content + chars
    
