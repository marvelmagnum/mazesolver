from window import Window
from maze import Maze

def main():
    win = Window(800, 600)

    num_cols = 16
    num_rows = 12

    maze = Maze(25, 25, num_rows, num_cols, 45, 45, win)
    maze.solve()
    # while not maze.solve():
    #     win._canvas.delete("all")
    #     maze = Maze(25, 25, num_rows, num_cols, 20, 20, win)
    
    win.wait_for_close()

if __name__ == '__main__':
    main()