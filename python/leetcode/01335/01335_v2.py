"""
1335. Minimum Difficulty of a Job Schedule
Hard

"""
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        t = []  # d x n
        t.append([-1 for _ in range(n + 1)])
        t[0][0] = 0
        for d_i in range(1, d + 1):

            tr = [-1 for _ in range(n + 1)]
            t.append(tr)
            for e in range(0, n + 1):
                tr[e] = -1
                cur_job_cost = jobDifficulty[e - 1]
                for s in range(e - 1, -1, -1):
                    cur_job_cost = max(cur_job_cost, jobDifficulty[s])
                    if t[d_i - 1][s] == -1:
                        continue
                    new_val = t[d_i - 1][s] + cur_job_cost
                    if tr[e] == -1 or tr[e] > new_val:
                        tr[e] = new_val
        print(t)
        return t[d][n]


"""
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        table = [] # d x n
        table.append([-1 for _ in range(n)])
        table[0][0] = 0
        table.append([max(jobDifficulty[:x+1]) for x in range(n)])
        for i_d in range(2, d+1):
            table.append([-1 for _ in range(n)])
            for c in range(0, n):
                max_to_the_right = max(jobDifficulty[c:])
                subtask = table[i_d-1][c-1]
                if c > 0 and subtask != -1:
                    new_val = max_to_the_right + subtask
                    if table[i_d][c] == -1 or table[i_d][c] > new_val:
                        table[i_d][c] = new_val
        print(table)
        return (table[d][n-1])
"""

"""
 0  1  2  3  4  5  6
 7  1  7  1  7  8

stdout
[
[0, -1, -1, -1, -1, -1, -1],
[-1, 7, 7, 7, 7, 7, 8], 
[-1, -1, 8, 14, 8, 14, 15], 
[-1, -1, -1, 15, 15, 15, 16],
[-1, -1, -1, -1, 16, 22, 23]
]



"""
