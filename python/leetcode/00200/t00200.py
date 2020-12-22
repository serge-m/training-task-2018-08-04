"""
200. Number of Islands
medium

Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
"""
from typing import List

land = '1'


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [
            [0 for i in range(m)]
            for j in range(n)
        ]
        counter = 0
        for y in range(n):
            for x in range(m):
                if not visited[y][x] and grid[y][x] == land:
                    counter += 1
                    search(y, x, grid, visited, counter)
        return counter


moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def search(y, x, grid, visited, counter):
    if visited[y][x]:
        return
    visited[y][x] = counter
    n = len(grid)
    m = len(grid[0])

    for move in moves:
        ny, nx = y + move[0], x + move[1]
        if 0 <= ny < n and 0 <= nx < m and grid[y][x] == land:
            search(ny, nx, grid, visited, counter)
