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
            win
    ):
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = None
        
    def _create_cells(self):
        for i in range(0, self._num_rows):
            row = []
            for j in range(0, self._num_cols):
                x1 = self._x + (self._cell_size_x * i)
                y1 = self._y + (self._cell_size_y * j)
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
                row.append(Cell(x1, y1, x2, y2, self._win))
            self._cells.append(row)

    def _draw_cell(self)