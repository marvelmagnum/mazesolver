import time
import random
from cell import Cell

class Maze:
    def __init__(
            self,
            x,
            y,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
    ):
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = None
        if seed:
            random.seed(seed)
        
    def _generate_cells(self):
        print(self._num_rows, self._num_cols)
        self._cells = []
        for i in range(0, self._num_rows):
            row = []
            for j in range(0, self._num_cols):
                x1 = self._x + (self._cell_size_x * j)
                y1 = self._y + (self._cell_size_y * i)
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
                cell = Cell(x1, y1, x2, y2, self._win)
                row.append(cell)
                if self._win:
                    cell.draw()
            self._cells.append(row)

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw()
        self._cells[self._num_rows-1][self._num_cols-1].has_bottom_wall = False
        self._cells[self._num_rows-1][self._num_cols-1].draw()