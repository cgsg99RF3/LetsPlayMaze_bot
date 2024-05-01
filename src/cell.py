class Cell:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.is_checked = False
        self.walls = {'top': True, 'bottom': True, 'right': True, 'left': True}
        self.in_path = False

    def get_neighbours(self, grid: list) -> list:
        neighbours = []

        if self.x + 1 < len(grid) and not (grid[self.x + 1][self.y].is_checked):
            neighbours.append(grid[self.x + 1][self.y])
        if self.x - 1 >= 0 and not (grid[self.x - 1][self.y].is_checked):
            neighbours.append(grid[self.x - 1][self.y])
        if self.y + 1 < len(grid[self.x]) and not (grid[self.x][self.y + 1].is_checked):
            neighbours.append(grid[self.x][self.y + 1])
        if self.y - 1 >= 0 and not (grid[self.x][self.y - 1].is_checked):
            neighbours.append(grid[self.x][self.y - 1])
        return neighbours

    def get_used_neighbours(self, grid: list) -> list:
        neighbours = []

        if self.x + 1 < len(grid) and grid[self.x + 1][self.y].is_checked:
            neighbours.append(grid[self.x + 1][self.y])
        if self.x - 1 >= 0 and grid[self.x - 1][self.y].is_checked:
            neighbours.append(grid[self.x - 1][self.y])
        if self.y + 1 < len(grid[self.x]) and grid[self.x][self.y + 1].is_checked:
            neighbours.append(grid[self.x][self.y + 1])
        if self.y - 1 >= 0 and grid[self.x][self.y - 1].is_checked:
            neighbours.append(grid[self.x][self.y - 1])
        return neighbours

    @staticmethod
    def is_passage(first, second):
        dx = first.x - second.x
        dy = first.y - second.y

        if (dx == 1):
            return first.walls['right']
        if (dx == -1):
            return first.walls['left']
        if (dy == -1):
            return first.walls['bottom']
        if (dy == 1):
            return first.walls['top']

    @staticmethod
    def is_wall(first, second):
        return not Cell.is_passage(first, second)

    @staticmethod
    def set_path(first, second, is_wall):
        dx = first.x - second.x
        dy = first.y - second.y

        if (dx == -1):
            first.walls['right'] = is_wall
            second.walls['left'] = is_wall
        if (dx == 1):
            second.walls['right'] = is_wall
            first.walls['left'] = is_wall
        if (dy == -1):
            first.walls['bottom'] = is_wall
            second.walls['top'] = is_wall
        if (dy == 1):
            first.walls['top'] = is_wall
            second.walls['bottom'] = is_wall
