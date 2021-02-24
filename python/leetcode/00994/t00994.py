"""
994. Rotting Oranges
Medium

"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        FRESH = 1
        ROTTEN = 2
        m = len(grid)
        n = len(grid[0])
        new_rotten = [
            (y, x)
            for y in range(m)
            for x in range(n)
            if grid[y][x] == ROTTEN
        ]
        cnt = 0
        while True:

            rotten = new_rotten
            new_rotten = []
            for y, x in rotten:
                for ny, nx in [
                    (y + 1, x), (y, x + 1), (y - 1, x), (y, x - 1)
                ]:
                    if 0 <= ny < m and 0 <= nx < n and grid[ny][nx] == FRESH:
                        grid[ny][nx] = ROTTEN
                        new_rotten.append((ny, nx))
            if new_rotten:
                cnt += 1
            else:
                break
        if any((
                True
                for y in range(m)
                for x in range(n)
                if grid[y][x] == FRESH
        )):
            return -1
        return cnt
