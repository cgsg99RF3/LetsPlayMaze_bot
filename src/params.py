class Params:
    def __init__(self, width, height, maze_type):
        self.width = width
        self.height = height
        if maze_type == "DFS":
            self.type = 1

        elif maze_type == "MST":
            self.type = 2
