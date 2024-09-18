from window import Window
from maze import Maze

def main():
    win = Window(800, 600)

    num_cols = 12
    num_rows = 10
    maze = Maze(25, 25, num_rows, num_cols, 50, 50, win)
    maze._generate_cells()
    maze._break_entrance_and_exit()

    win.wait_for_close()

if __name__ == '__main__':
    main()