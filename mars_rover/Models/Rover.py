from Models.Grid import Grid


class RoverPosition:
    def __init__(self, x: int, y: int, direction: str):
        self.x = x
        self.y = y
        self.direction = direction

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.direction == other.direction


class MarsRover:
    def __init__(self, position: RoverPosition):
        self.position = position

    def move(self, grid: Grid, command: str) -> RoverPosition:
        wrap_position = RoverPosition(self.position.x, self.position.y, self.position.direction)
        for i in command:
            match self.position.direction, i:
                case "N", "M":
                    if grid.isobstacle(self.position.x, self.position.y + 1):
                        return self.position
                    self.position.y += 1
                    if self.position.y >= grid.size:
                        return wrap_position
                case "N", "L":
                    self.position.direction = "W"
                case "N", "R":
                    self.position.direction = "E"
                case "S", "M":
                    if grid.isobstacle(self.position.x, self.position.y - 1):
                        return self.position
                    self.position.y -= 1
                    if self.position.y < 0:
                        return wrap_position
                case "S", "L":
                    self.position.direction = "E"
                case "S", "R":
                    self.position.direction = "W"
                case "E", "M":
                    if grid.isobstacle(self.position.x + 1, self.position.y):
                        return self.position
                    self.position.x += 1
                    if self.position.x >= grid.size:
                        return wrap_position
                case "E", "L":
                    self.position.direction = "N"
                case "E", "R":
                    self.position.direction = "S"
                case "W", "M":
                    if grid.isobstacle(self.position.x - 1, self.position.y):
                        return self.position
                    self.position.x -= 1
                    if self.position.x < 0:
                        return wrap_position
                case "W", "L":
                    self.position.direction = "S"
                case "W", "R":
                    self.position.direction = "N"
        return self.position
