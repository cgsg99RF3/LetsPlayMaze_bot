from random import choice

from src.maze import Maze
from src.cell import Cell


class DFSMaze(Maze):
    def generate(self):
        cur_cell = self.grid[0][0]
        running_verts = []
        start = True

        while start or len(running_verts) != 0:
            start = False

            cur_cell.is_checked = True

            neighbours = cur_cell.get_neighbours(self.grid)
            if len(neighbours) > 0:
                next_cell = choice(neighbours)
                running_verts.append(cur_cell)
                Cell.set_path(cur_cell, next_cell, False)
                cur_cell = next_cell
            elif running_verts:
                cur_cell = running_verts.pop()
