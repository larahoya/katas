import unittest
from Models.Rover import *
from Models.Grid import *


class TestExamples(unittest.TestCase):

    def test_base(self):
        grid = Grid(10, [])
        rover = MarsRover(RoverPosition(0, 0, "N"))
        command = "MMRMMLM"
        result = rover.move(grid, command)
        expected = RoverPosition(2, 3, "N")
        self.assertEqual(result, expected)

    def test_wrap_around(self):
        grid = Grid(10, [])
        rover = MarsRover(RoverPosition(0, 0, "N"))
        command = "MMMMMMMMMM"
        result = rover.move(grid, command)
        expected = RoverPosition(0, 0, "N")
        self.assertEqual(result, expected)

    def test_obstacle(self):
        grid = Grid(10, [Point(0, 3)])
        rover = MarsRover(RoverPosition(0, 0, "N"))
        command = "MMMM"
        result = rover.move(grid, command)
        expected = RoverPosition(0, 2, "N")
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
