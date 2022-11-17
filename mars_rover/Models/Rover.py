from Models.Grid import Grid
from Models.Grid import Point
from enum import Enum


class Direction(str, Enum):
    north = 'N'
    south = 'S'
    east = 'E'
    west = 'W'


class MarsRover:
    def __init__(self, point: Point, direction: Direction):
        self.point = point
        self.direction = direction

    def move(self, grid: Grid, command: str) -> (Point, Direction):
        wrap_point, wrap_direction = Point(self.point.x, self.point.y), Direction(self.direction)
        for i in command:
            match self.direction, i:
                case Direction.north, "M":
                    if grid.isobstacle(self.point.x, self.point.y + 1):
                        return self.point, self.direction
                    self.point.y += 1
                    if self.point.y >= grid.size:
                        return wrap_point, wrap_direction
                case Direction.north, "L":
                    self.direction = Direction.west
                case Direction.north, "R":
                    self.direction = Direction.east
                case Direction.south, "M":
                    if grid.isobstacle(self.point.x, self.point.y - 1):
                        return self.point, self.direction
                    self.point.y -= 1
                    if self.point.y < 0:
                        return wrap_point, wrap_direction
                case Direction.south, "L":
                    self.direction = Direction.east
                case Direction.south, "R":
                    self.direction = Direction.west
                case Direction.east, "M":
                    if grid.isobstacle(self.point.x + 1, self.point.y):
                        return self.point, self.direction
                    self.point.x += 1
                    if self.point.x >= grid.size:
                        return wrap_point, wrap_direction
                case Direction.east, "L":
                    self.direction = Direction.north
                case Direction.east, "R":
                    self.direction = Direction.south
                case Direction.west, "M":
                    if grid.isobstacle(self.point.x - 1, self.point.y):
                        return self.point, self.direction
                    self.point.x -= 1
                    if self.point.x < 0:
                        return wrap_point, wrap_direction
                case Direction.west, "L":
                    self.direction = Direction.south
                case Direction.west, "R":
                    self.direction = Direction.north
        return self.point, self.direction
