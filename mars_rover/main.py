from Models.Rover import *
from Models.Grid import *

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # base
    roverGrid1 = Grid(10, [])
    rover1 = MarsRover(RoverPosition(0, 0, "N"))
    command1 = "MMRMMLM"
    rover1.move(roverGrid1, command1).print()

    # wrap-around
    roverGrid2 = Grid(10, [])
    rover2 = MarsRover(RoverPosition(0, 0, "N"))
    command2 = "MMMMMMMMMM"
    rover2.move(roverGrid2, command2).print()

    # obstacles
    roverGrid3 = Grid(10, [Point(0, 3)])
    rover3 = MarsRover(RoverPosition(0, 0, "N"))
    command3 = "MMMM"
    rover3.move(roverGrid3, command3).print()
