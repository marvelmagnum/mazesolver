from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self._root = Tk()
        self._root.title("Maze Solver")
        self._root.geometry(f"{width}x{height}")
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._canvas = Canvas()
        self._canvas.pack(side="left")
        self._canvas.pack(fill='both')
        self._canvas.pack(expand=1)
        self._running = False

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()

    def close(self):
        self._running = False

    def draw_line(self, line, color):
        line.draw(self._canvas, color)
