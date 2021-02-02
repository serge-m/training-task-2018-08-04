"""
1041. Robot Bounded In Circle
Medium

t=23
"""

import numpy as np


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        g = np.array([
            [1, 0, 0],
            [0, 1, 1],
            [0, 0, 1]
        ])
        l = np.array([
            [0, -1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ])
        r = np.array([
            [0, 1, 0],
            [-1, 0, 0],
            [0, 0, 1]
        ])

        m = {'G': g, 'L': l, 'R': r}

        def sum_commands(instructions):
            res = np.eye(3, dtype='int')
            for i in instructions:
                res = m[i] @ res
            return res

        sum_of_commands = sum_commands(instructions)
        # print(sum_commands)
        no_rotation = np.array_equal(sum_of_commands[:2, :2], [[1, 0], [0, 1]])
        translation_exists = sum_of_commands[0, 2] != 0 or sum_of_commands[1, 2] != 0
        if no_rotation and translation_exists:
            return False
        return True


"""
0, 0 -> 0, a -> loop
0, 0 -> x 0 -> unbound
0, 0 -> x 180 -> loop
0, 0 -> (x, y) 90 ->  (x + y, y - x, 180 ) -> loop


"""

