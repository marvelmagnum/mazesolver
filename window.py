from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.geometry(f"{self.width}x{self.height}")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas()
        self.__canvas.pack()
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

def main():
    win = Window(800, 600)
    win.wait_for_close()

if __name__ == '__main__':
    main()