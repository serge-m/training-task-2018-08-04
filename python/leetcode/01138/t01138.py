"""
1138. Alphabet Board Path
Medium

"""


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]

        c2row = {}
        c2col = {}
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                c2row[c] = i
                c2col[c] = j

        def get_path(start, end):
            if start == 'z':
                return 'U' * (c2row['z'] - c2row[end]) + 'R' * c2col[end]
            res = ""

            move = c2col[end] - c2col[start]
            if move > 0:
                res += 'R' * move
            else:
                res += 'L' * (-move)

            move = c2row[end] - c2row[start]
            if move > 0:
                res += 'D' * move
            else:
                res += 'U' * (-move)

            return res

        pos = 'a'
        result = []
        for c in target:
            result.append(get_path(pos, c))
            result.append('!')
            pos = c
        return ''.join(result)
