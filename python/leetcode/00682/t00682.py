"""
682. Baseball Game
Easy

t=6
"""


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []
        for op in ops:
            try:
                op_int = int(op)
            except ValueError:
                op_int = None

            if op_int is not None:
                scores.append(op_int)
                continue

            if op == "D":
                scores.append(scores[-1] * 2)
                continue

            if op == "C":
                scores.pop()
                continue

            if op == "+":
                scores.append(scores[-2] + scores[-1])
                continue

        return sum(scores, 0)
