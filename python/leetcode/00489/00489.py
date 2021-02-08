"""
489. Robot Room Cleaner
Hard
"""

"""
class Robot:
  def move(self):
    return false 
  def turnLeft(self):
    pass
  def turnRight(self):
    pass
  def clean(self):
    pass
"""

from dataclasses import dataclass


@dataclass(eq=True, frozen=True)
class Pos:
    y: int
    x: int

    def __add__(self, direction):
        return Pos(self.y + direction[0], self.x + direction[1])


UP = (-1, 0)
LEFT = (0, -1)
DOWN = (1, 0)
RIGHT = (0, 1)


def abs_step(direction):
    return direction


def probe_direction(robot, direction):
    if direction is UP:
        pass
    if direction is LEFT:
        robot.turnLeft()
    if direction is DOWN:
        robot.turnLeft()
        robot.turnLeft()
    if direction is RIGHT:
        robot.turnRight()
    return robot.move()


def reverse_probe(robot, direction):
    if direction is UP:
        # do nothing
        return
    if direction is LEFT:
        robot.turnRight()
    if direction is DOWN:
        robot.turnLeft()
        robot.turnLeft()
    if direction is RIGHT:
        robot.turnLeft()


def reverse_move(robot, direction):
    # initial direction is up
    if direction is UP:
        robot.turnLeft()
        robot.turnLeft()
        robot.move()
        robot.turnLeft()
        robot.turnLeft()
    if direction is LEFT:
        robot.turnRight()
        robot.move()
        robot.turnLeft()
    if direction is DOWN:
        robot.move()
    if direction is RIGHT:
        robot.turnLeft()
        robot.move()
        robot.turnRight()


class Solution:
    def __init__(self):
        self.env = {}

    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        assert not self.env
        pos = Pos(0, 0)
        self.cleanRoom_(robot, pos)

    def try_go(self, robot, pos, direction):
        old_pos = pos
        next_pos = pos + direction
        if self.env.get(next_pos, 0) != 0:
            return
        free = probe_direction(robot, direction)
        if not free:
            self.env[next_pos] = 1
            reverse_probe(robot, direction)
            return
        reverse_probe(robot, direction)
        pos = next_pos
        self.cleanRoom_(robot, pos)
        reverse_move(robot, direction)

    def cleanRoom_(self, robot, pos):
        # prereq: robot on a cell, upright
        robot.clean()
        self.env[pos] = 2
        for direction in [UP, LEFT, DOWN, RIGHT]:
            self.try_go(robot, pos, direction)
