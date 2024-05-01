from src.params import Params
from src.maze import Maze
from src.dfs_maze import DFSMaze
from src.mst_maze import MSTMaze

from aiogram.types import Message


class Player:
    def __init__(self, message: Message):
        self.pos = [-1, -1]
        self.id = message.from_user.id
        self.param = Params
        self.maze = Maze

    def create_maze(self, width, height, maze_type):
        self.param = Params((width + 1) // 2, (height + 1) // 2, maze_type)
        if self.param.type == 1:
            self.maze = DFSMaze(self.param)
        elif self.param.type == 2:
            self.maze = MSTMaze(self.param)
        self.maze.generate()

    def move(self, delta):
        x = self.pos[0] // 2
        y = self.pos[1] // 2
        flg = False
        if (self.pos[0] + delta[0]) % 2 == 1 and (self.pos[1] + delta[1]) % 2 == 1:
            return
        if self.pos[0] % 2 == 0 and self.pos[1] % 2 == 0:
            if delta == [1, 0] and not self.maze.grid[x][y].walls['right']:
                flg = True
            elif delta == [-1, 0] and not self.maze.grid[x][y].walls['left']:
                flg = True
            elif delta == [0, 1] and not self.maze.grid[x][y].walls['bottom']:
                flg = True
            elif delta == [0, -1] and not self.maze.grid[x][y].walls['top']:
                flg = True
        else:
            flg = True
        if flg:
            self.pos[0] += delta[0]
            self.pos[1] += delta[1]

    def check(self):
        if (self.pos[0] // 2 == len(self.maze.grid) - 1 and
                self.pos[1] // 2 == len(self.maze.grid[0]) - 1):
            return True
        return False

    def draw(self):
        grid = '\n'
        for i in range(len(self.maze.grid) * 2 + 1):
            grid += '🦠'
        grid += '\n'
        for y in range(len(self.maze.grid[0])):
            grid += '🦠'
            for x in range(len(self.maze.grid)):
                cell = self.maze.grid[x][y]
                if (self.pos[0] % 2 == 0 and self.pos[1] % 2 == 0 and
                        cell.x == self.pos[0] // 2 and cell.y == self.pos[1] // 2):
                    grid += '👽'
                elif cell.in_path:
                    grid += '👾'
                else:
                    grid += '⬜'
                if (self.pos[0] % 2 == 1 and self.pos[1] % 2 == 0 and
                        cell.y == self.pos[1] // 2 and cell.x == self.pos[0] // 2):
                    grid += '👽'
                elif not cell.walls['right']:
                    if cell.in_path and x != len(self.maze.grid) - 1 and self.maze.grid[x + 1][y].in_path:
                        grid += '👾'
                    elif y == len(self.maze.grid[0]) - 1 and x == len(self.maze.grid) - 1:
                        grid += '🪬'
                    else:
                        grid += '⬜'
                else:
                    grid += '🦠'
            grid += '\n'
            grid += '🦠'
            for x in range(len(self.maze.grid)):
                cell = self.maze.grid[x][y]
                if (self.pos[1] % 2 == 1 and self.pos[0] % 2 == 0 and
                        cell.y == self.pos[1] // 2 and cell.x == self.pos[0] // 2):
                    grid += '👽'
                elif not cell.walls['bottom']:
                    if (cell.in_path and y != len(self.maze.grid[0]) - 1 and
                            self.maze.grid[x][y + 1].in_path):
                        grid += '👾'
                    else:
                        grid += '️⬜'
                else:
                    grid += '🦠'
                grid += '🦠'
            grid += '\n'
        return grid
