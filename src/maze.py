from abc import ABC, abstractmethod

from src.params import Params
from src.cell import Cell


class Maze():
    def __init__(self, params: Params):
        self.params = params
        mn_sz = max(params.height, params.width)
        self.grid = [[Cell(x, y) for y in range(params.height)] for x in
                     range(params.width)]
        if len(self.grid) != 0:
            self.grid[params.width - 1][params.height - 1].walls['right'] = False

    @abstractmethod
    def generate(self):
        pass
