from src.maze import Maze


class Path:
    def __init__(self, maze: Maze):
        self.used = [[False for y in range(maze.params.height)] for x in range(maze.params.width)]
        self.counter = 0

    def find(self, x, y, maze):
        self.counter += 1
        if self.counter > maze.params.height * maze.params.width:
            return False
        cell = maze.grid[x][y]
        self.used[x][y] = True

        if x == (maze.params.width - 1) and y == (maze.params.height - 1):
            maze.grid[x][y].in_path = True
            return True

        if not cell.walls['left'] and not self.used[x - 1][y]:
            if self.find(x - 1, y, maze):
                maze.grid[x][y].in_path = True
                return True
        if not cell.walls['right'] and not self.used[x + 1][y]:
            if self.find(x + 1, y, maze):
                maze.grid[x][y].in_path = True
                return True
        if not cell.walls['top'] and not self.used[x][y - 1]:
            if self.find(x, y - 1, maze):
                maze.grid[x][y].in_path = True
                return True
        if not cell.walls['bottom'] and not self.used[x][y + 1]:
            if self.find(x, y + 1, maze):
                maze.grid[x][y].in_path = True
                return True
        return False
