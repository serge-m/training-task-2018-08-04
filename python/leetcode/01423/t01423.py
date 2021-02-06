"""
1423. Maximum Points You Can Obtain from Cards
Medium

t=15
"""

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        sum_taken = 0
        for i in range(n-k, n):
            sum_taken += cardPoints[i]
        best_sum_taken = sum_taken

        for take_from_start in range(0, k):
            sum_taken = sum_taken + cardPoints[take_from_start] - cardPoints[take_from_start+n-k]
            best_sum_taken = max(best_sum_taken, sum_taken)
        return best_sum_taken
