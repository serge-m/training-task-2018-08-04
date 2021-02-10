"""
302. Smallest Rectangle Enclosing Black Pixels
Hard

linear O(mn)

can be solved faster with bincary search

"""


class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        m = len(image)
        n = len(image[0])

        moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        minx = x
        maxx = x
        miny = maxy = y

        def dfs(x, y):
            # print("dfs", x, y)
            nonlocal minx, maxx, miny, maxy
            minx = min(minx, x)
            maxx = max(maxx, x)
            miny = min(miny, y)
            maxy = max(maxy, y)

            image[x][y] = "2"
            for dx, dy in moves:
                x2 = x + dx
                y2 = y + dy
                # print("-> ", x2, y2)
                if 0 <= x2 < m and 0 <= y2 < n:
                    # print(image[x2][y2])
                    if image[x2][y2] == "1":
                        dfs(x2, y2)
            # print(x, y)
            # print(image)

        dfs(x, y)

        return (maxx - minx + 1) * (maxy - miny + 1)
