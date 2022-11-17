import unittest
from Models.Rover import *
from Models.Grid import *


class TestExamples(unittest.TestCase):

    def test_base(self):
        rover = MarsRover(Point(0, 0), Direction.north, Grid(10, []))
        command = "MMRMMLM"
        result_point, result_direction = rover.execute(command)
        expected_point, expected_direction = Point(2, 3), Direction.north
        self.assertEqual(result_point, expected_point)
        self.assertEqual(result_direction, expected_direction)

    def test_wrap_around(self):
        rover = MarsRover(Point(0, 0), Direction.north, Grid(10, []))
        command = "MMMMMMMMMM"
        result_point, result_direction = rover.execute(command)
        expected_point, expected_direction = Point(0, 0), Direction.north
        self.assertEqual(result_point, expected_point)
        self.assertEqual(result_direction, expected_direction)

    def test_obstacle(self):
        rover = MarsRover(Point(0, 0), Direction.north, Grid(10, [Point(0, 3)]))
        command = "MMMM"
        result_point, result_direction = rover.execute(command)
        expected_point, expected_direction = Point(0, 2), Direction.north
        self.assertEqual(result_point, expected_point)
        self.assertEqual(result_direction, expected_direction)


if __name__ == '__main__':
    unittest.main()
