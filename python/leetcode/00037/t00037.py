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

        available = Available.from_busy(
            cols=[b[:, i] for i in range(9)],
            rows=[b[i, :] for i in range(9)],
            sq=[
                [
                    b[i:i + 3, j:j + 3].ravel()
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


class Available:
    def __init__(self, in_cols, in_rows, in_sq):
        self.in_cols = in_cols
        self.in_rows = in_rows
        self.in_sq = in_sq

    @staticmethod
    def from_busy(cols, rows, sq):
        return Available(
            in_cols=[set(all_9) - set(col) for col in cols],
            in_rows=[set(all_9) - set(row) for row in rows],
            in_sq=[
                [
                    set(all_9) - set(sq[i][j])
                    for j in range(0, 3)
                ]
                for i in range(0, 3)
            ]
        )

    def get_state(self, pos):
        old_in_rows = self.in_rows[pos[0]]
        old_in_cols = self.in_cols[pos[1]]
        old_in_sq = self.in_sq[pos[0] // 3][pos[1] // 3]
        return old_in_rows, old_in_cols, old_in_sq

    def set_state(self, pos, state):
        in_rows, in_cols, in_sq = state
        self.in_rows[pos[0]] = in_rows
        self.in_cols[pos[1]] = in_cols
        self.in_sq[pos[0] // 3][pos[1] // 3] = in_sq


def available_from_state(state):
    in_rows, in_cols, in_sq = state
    return in_rows.intersection(in_cols).intersection(in_sq)


def state_minus(state, value):
    value = {value}
    in_rows, in_cols, in_sq = state
    return in_rows.difference(value), in_cols.difference(value), in_sq.difference(value)


def step_right(pos):
    return pos[0], pos[1] + 1


def search(b, pos: Tuple[int, int], available):
    if pos[1] == 9:
        pos = (pos[0] + 1, 0)

    if pos[0] == 9:
        return True

    nxt = step_right(pos)
    if b[pos] != empty:
        return search(b, nxt, available)

    old_state = available.get_state(pos)
    actions = available_from_state(old_state)
    for action in actions:
        b[pos] = action
        available.set_state(pos, state_minus(old_state, action))
        if search(b, nxt, available):
            return True

    b[pos] = empty
    available.set_state(pos, old_state)

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


def test_profiling():
    import cProfile

    with cProfile.Profile() as pr:
        for i in range(100):
            test_default()

    pr.print_stats()
