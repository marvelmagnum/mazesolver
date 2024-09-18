from window import Window
from point import Point
from line import Line
from cell import Cell

def main():
    win = Window(800, 600)

    cell1 = Cell(100,50, 150,100, win, has_bottom_wall=False)
    cell2 = Cell(150,100, 200,150, win, has_left_wall=False)
    cell3 = Cell(50,100, 100,150, win, has_right_wall=False)
    cell4 = Cell(100,150, 150,200, win, has_top_wall=False)

    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell4.draw()

    cell2.draw_move(cell3, True)
    cell1.draw_move(cell4, False)

    win.wait_for_close()

if __name__ == '__main__':
    main()