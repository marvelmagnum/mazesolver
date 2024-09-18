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

        self._generate_cells()
        self._break_walls_r(0,0)
        self._break_entrance_and_exit()
        self._reset_cells_visited()

        
    def _generate_cells(self):
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
            self._cells.append(row)

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw()
        self._cells[self._num_rows-1][self._num_cols-1].has_bottom_wall = False
        self._cells[self._num_rows-1][self._num_cols-1].draw()

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self._num_rows - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self._num_cols - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self._cells[i][j].draw()
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # up
            if next_index[0] == i - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i - 1][j].has_bottom_wall = False
            # down
            if next_index[0] == i + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i + 1][j].has_top_wall = False
            # left
            if next_index[1] == j - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i][j - 1].has_right_wall = False
            # right
            if next_index[1] == j + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i][j + 1].has_left_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])


    def _reset_cells_visited(self):
        for i in range(0, self._num_rows):
            for j in range(0, self._num_cols):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self,i, j):
        self._animate()
        self._cells[i][j].visited = True
        
        if i == self._num_rows - 1 and j == self._num_cols - 1:
            return True
        
        # Check bottom
        if not self._cells[i][j].has_bottom_wall and not self._cells[i+1][j].visited:
            #print(f"{i}/{j}-> Going Bottom")
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            else:
                #print(f"{i}/{j}-> Going Bottom (Undo)")
                self._cells[i][j].draw_move(self._cells[i+1][j], True)

        # Check right
        if not self._cells[i][j].has_right_wall and not self._cells[i][j+1].visited:
            #print(f"{i}/{j}-> Going Right")
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            else:
                #print(f"{i}/{j}-> Going Right (Undo)")
                self._cells[i][j].draw_move(self._cells[i][j+1], True)       
        
        # Check left
        if not self._cells[i][j].has_left_wall and not self._cells[i][j-1].visited:
            #print(f"{i}/{j}-> Going Left")
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            else:
                #print(f"{i}/{j}-> Going Left (Undo)")
                self._cells[i][j].draw_move(self._cells[i][j-1], True)

        # Check top
        if not (i == 0 and j == 0) and not self._cells[i][j].has_top_wall and not self._cells[i-1][j].visited:
            #print(f"{i}/{j}-> Going Top")
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            else:
                #print(f"{i}/{j}-> Going Top (Undo)")
                self._cells[i][j].draw_move(self._cells[i-1][j], True)

        return False
        
