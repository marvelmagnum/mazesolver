import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_generate_cells(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(maze._cells), num_rows)
        self.assertEqual(len(maze._cells[0]), num_cols)

    def test_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertFalse(maze._cells[0][0].has_top_wall)
        self.assertFalse(maze._cells[num_rows-1][num_cols-1].has_bottom_wall)

    def test_reset_visited(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        for i in range(0, num_rows):
            for j in range(0, num_cols):
                self.assertFalse(maze._cells[i][j].visited)


if __name__ == "__main__":
    unittest.main()