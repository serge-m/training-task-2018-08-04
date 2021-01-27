"""
1629. Slowest Key
Easy

t = 9
"""
from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        assert len(releaseTimes) == len(keysPressed), "wrong input"
        assert len(keysPressed) > 0
        best_duration = 0
        best_key = None
        for i, (t, k) in enumerate(zip(releaseTimes, keysPressed)):
            duration = releaseTimes[i] - releaseTimes[i - 1] if i > 0 else releaseTimes[i]
            if (duration, k) > (best_duration, best_key):
                (best_duration, best_key) = duration, k

        return best_key
