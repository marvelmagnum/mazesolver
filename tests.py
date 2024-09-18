import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_generate_cells(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        maze._generate_cells()
        self.assertEqual(len(maze._cells), num_rows)
        self.assertEqual(len(maze._cells[0]), num_cols)


if __name__ == "__main__":
    unittest.main()