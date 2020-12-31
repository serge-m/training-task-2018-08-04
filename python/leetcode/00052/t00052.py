"""
52. N-Queens II
Hard
"""
from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        board = Board(n)
        board.find(0)
        return len(board.converted_solutions())


class Board:
    def __init__(self, n):
        self.n = n
        self.vertical = [-1 for _ in range(n)]
        self.solutions = []

    def find(self, line):
        if line == self.n:
            self.solutions.append(self.vertical[:])
            return

        for i in range(self.n):
            if self.vertical[i] == -1 and self.ok_diagonals(line, i):
                self.vertical[i] = line
                self.find(line + 1)
                self.vertical[i] = -1

    def ok_diagonals(self, line, pos):
        for i in range(1, line + 1):
            target_pos = pos + i
            target_line = line - i
            if target_pos >= self.n:
                break
            if target_line < 0:
                break
            if self.vertical[target_pos] == target_line:
                return False

        for i in range(1, line + 1):
            target_pos = pos - i
            target_line = line - i
            if target_pos < 0:
                break
            if target_line < 0:
                break
            if self.vertical[target_pos] == target_line:
                return False

        return True

    def converted_solutions(self):
        return [
            self._convert_solution(sol) for sol in self.solutions
        ]

    @staticmethod
    def _convert_solution(solution):
        def _convert_line(pos):
            s = [".", ] * len(solution)
            s[pos] = 'Q'
            return ''.join(s)

        return [
            _convert_line(pos) for pos in solution
        ]



