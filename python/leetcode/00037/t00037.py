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

        search(b, (0, 0))

        board[:] = [
            [
                str(x) if x != empty else '.'
                for x in row
            ]
            for row in b
        ]


def next_pos(pos: Tuple[int, int]) -> Tuple[int, int]:
    if pos[1] == 8:
        return pos[0] + 1, 0
    return pos[0], pos[1] + 1


def line_ok(b, row_idx):
    return sorted(b[row_idx]) == all_9


def columns_ok(b):
    return True


def square_ok(square):
    return sorted(square.ravel()) == all_9


def squares_ok(b, row_idx):
    rows = b[row_idx: row_idx + 3]
    return square_ok(rows[:, 0:3]) and square_ok(rows[:, 3:6]) and square_ok(rows[:, 6:9])


def step_right(pos):
    return pos[0], pos[1] + 1


def lock_action(action, pos):
    pass


def get_actions(b, pos):
    actions = set(range(1, 10))
    for x in b[pos[0]]:
        if x != 0:
            actions.discard(x)
    for x in b[:, pos[1]]:
        if x != 0:
            actions.discard(x)
    sq_y, sq_x = (pos[0] // 3) * 3, (pos[1] // 3) * 3
    for x in b[sq_y:sq_y + 3, sq_x:sq_x + 3].ravel():
        if x != 0:
            actions.discard(x)

    return actions


def search(b, pos):
    y, x = pos
    if y == 9:
        return columns_ok(b)
    if x == 9:
        if not line_ok(b, y):
            return False
        return search(b, (y + 1, 0))
    if y in (2, 5, 8) and x in (3, 6, 9):
        if not square_ok(b[y - 2:y + 1, x - 3:x]):
            return False

    nxt = step_right(pos)
    if b[pos] != empty:
        return search(b, nxt)

    old = b[pos]
    actions = get_actions(b, pos)
    for action in actions:
        b[pos] = action

        if search(b, nxt):
            return True

    b[pos] = old
    return False


def test_default():
    board = [
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
    sol.solveSudoku(board)

    assert board == expected


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

    assert get_actions(b, (0, 5)) == {6, 8}
