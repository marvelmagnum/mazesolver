from point import Point
from line import Line

class Cell:
    def __init__(
            self,
            x1=0, y1=0, x2=0, y2=0, 
            win=None,
            has_left_wall=True,
            has_right_wall=True,
            has_top_wall=True,
            has_bottom_wall=True
    ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        self.visited = False

    def set_pos(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

    def draw(self):
        if not self._win:
            return
        
        color_top = "black" if self.has_top_wall else "#d9d9d9"
        color_bottom = "black" if self.has_bottom_wall else "#d9d9d9"
        color_left = "black" if self.has_left_wall else "#d9d9d9"
        color_right = "black" if self.has_right_wall else "#d9d9d9"

        self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), color_top)
        self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), color_bottom)
        self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), color_left)
        self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), color_right)

    def draw_move(self, to_cell, undo=False):
        color = "red" if undo is False else "gray"
        mid_from = Point((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)
        mid_to = Point((to_cell._x1 + to_cell._x2) // 2, (to_cell._y1 + to_cell._y2) // 2)
        path = Line(mid_from, mid_to)
        self._win.draw_line(path, color)