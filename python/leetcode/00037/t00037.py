import copy
from time import time
from typing import List, Tuple
import numpy as np

empty = 0
all_9 = list(range(1, 10))


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Rules:
            Each of the digits 1-9 must occur exactly once in each row.
            Each of the digits 1-9 must occur exactly once in each column.
            Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
        """

        b = np.array([[int(x) if x != '.' else empty for x in row] for row in board], dtype='int')

        available = Available(
            in_cols=[set(all_9) - set(b[:, i]) for i in range(9)],
            in_rows=[set(all_9) - set(b[i, :]) for i in range(9)],
            in_sq=[
                [
                    set(all_9) - set(b[i:i + 3, j:j + 3].ravel())
                    for j in range(0, 9, 3)
                ]
                for i in range(0, 9, 3)
            ]
        )
        search(b, (0, 0), available)

        board[:] = [
            [
                str(x) if x != empty else '.'
                for x in row
            ]
            for row in b
        ]


def or_default(x, default):
    return x if x is not None else default


class Available:
    def __init__(self, in_cols, in_rows, in_sq):
        self.in_cols = or_default(in_cols, [set(all_9) for i in range(9)])
        self.in_rows = or_default(in_rows, [set(all_9) for i in range(9)])
        self.in_sq = or_default(in_sq, [[set(all_9) for i in range(3)] for j in range(3)])


def step_right(pos):
    return pos[0], pos[1] + 1


def actions_square(b, pos):
    sq_y, sq_x = (pos[0] // 3) * 3, (pos[1] // 3) * 3
    return set(b[sq_y:sq_y + 3, sq_x:sq_x + 3].ravel())


def actions_row(b, pos):
    return set(b[pos[0]])


def actions_col(b, pos):
    return set(b[:, pos[1]])


def search(b, pos: Tuple[int, int], available):
    if pos[1] == 9:
        pos = (pos[0] + 1, 0)

    if pos[0] == 9:
        return True

    nxt = step_right(pos)
    if b[pos] != empty:
        return search(b, nxt, available)

    old_in_rows = available.in_rows[pos[0]]
    old_in_cols = available.in_cols[pos[1]]
    old_in_sq = available.in_sq[pos[0] // 3][pos[1] // 3]
    actions = old_in_rows.intersection(old_in_cols).intersection(old_in_sq)
    for action in actions:
        b[pos] = action
        available.in_rows[pos[0]] = old_in_rows - {action}
        available.in_cols[pos[1]] = old_in_cols - {action}
        available.in_sq[pos[0] // 3][pos[1] // 3] = old_in_sq - {action}
        if search(b, nxt, available):
            return True

    b[pos] = empty
    available.in_rows[pos[0]] = old_in_rows
    available.in_cols[pos[1]] = old_in_cols
    available.in_sq[pos[0] // 3][pos[1] // 3] = old_in_sq

    return False


def test_default():
    board0 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    expected = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]

    sol = Solution()

    board = copy.deepcopy(board0)
    start = time()
    sol.solveSudoku(board)
    elapsed = time() - start
    print(elapsed)
    assert board == expected

    board = copy.deepcopy(board0)[::-1]
    start = time()
    sol.solveSudoku(board)
    elapsed = time() - start
    print(elapsed)
    assert board == expected[::-1]


def test_get_actions():
    b = np.array([
        [5, 3, 4, 2, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]])

    pos = (0, 5)
    assert set(all_9) - actions_col(b, pos) - actions_row(b, pos) - actions_square(b, pos) == {6, 8}
