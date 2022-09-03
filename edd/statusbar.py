from buffer import Buffer

def statusbar(cols: int, filename: str, pos_y: int, pos_x: int , buffer: Buffer) -> None:
    
    buffer.add("\x1b[7m")
    bar_len = len(filename)
    
    buffer.add(filename)
    while (bar_len < cols):
        cur_pos = f"{pos_y + 1},{pos_x + 1}"

        if bar_len == int(cols / 2) - len(cur_pos):
            buffer.add(cur_pos)
            bar_len += len(cur_pos)

        else:
            buffer.add(" ")
            bar_len += 1

    buffer.add("\x1b[m")
