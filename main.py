import os
from typing import List

cols, rows = os.get_terminal_size()

options = ["Option 1", "Option 2", "Option 3", "Option 4"]

def init():
    print("\33[2J")
    print(f"\33[1;1H", end="")

def displayMenu(menu:List):
    
    print("________\n")
    for item in menu:
        print(item)
    
def main():
    init()
    displayMenu(options)
    input("")

if __name__ == "__main__":
    main()
