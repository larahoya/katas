class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Grid:
    def __init__(self, size: int, obstacles: list):
        self.size = size
        self.obstacles = obstacles

    def isobstacle(self, x: int, y: int) -> bool:
        return True if Point(x, y) in self.obstacles else False
