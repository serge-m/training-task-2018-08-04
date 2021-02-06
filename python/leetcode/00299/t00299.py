"""
299. Bulls and Cows
Medium

t = 7
"""
from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        x = 0
        cnt_s = Counter()
        cnt_g = Counter()

        for s, g in zip(secret, guess):
            if s == g:
                x += 1
            else:
                cnt_s[s] += 1
                cnt_g[g] += 1

        y = 0
        for c in cnt_s.keys():
            y += min(cnt_s[c], cnt_g[c])
        return f"{x}A{y}B"


