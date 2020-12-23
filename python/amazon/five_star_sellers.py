"""
Given a sum of ratios:
S = a_1 / b_1 + a_2 / b_2 + ... + a_n / b_n
and a threshold.

1<=Threshold<100

a_i, b_i are integers,

0 <= a_i < b_i <= 100
1 <= n <= 100

In one turn one can change one of the ratios so that
a_i / b_i becomes (a_i + 1) / (b_i + 1)

What is the minimum amount of turns required to make S >= (threshold / 100.)?


Example:
    ratios are defined as an array: [[4,4], [1,2], [3, 6]]
    threshold = 77.


Initially S = ((4 / 4) + (1/2) + (3/6))/3 = 66.66%
If we change the second ratio: S_1 = ((4 / 4) + (2/3) +(3/6))/3 = 72.22%
We change the second ratio again: S_2 =  ((4 / 4) + (3/4) + (3/6))/3 = 75.00%
We change the third ratio: S_3 = ((4/4) + (3/4) + (4/7))/3 = 77.38%
At this point, the threshold of 77% is reached.
The answer is 3 because it is the minimum amount of turns required to meet the threshold.


"""


import heapq


class Solution:
    def fiveStarReviews(self, productRatings, ratingsThreshold):
        increments = [self.rating_gain(r) for r in productRatings]
        q = [(-increment, i) for i, increment in enumerate(increments)]
        heapq.heapify(q)

        cnt = 0
        while True:
            s = sum((a / b for a, b in productRatings), 0.)
            if s * 100 >= ratingsThreshold * len(productRatings):
                return cnt
            cnt += 1

            (_, i) = heapq.heappop(q)
            productRatings[i][0] += 1
            productRatings[i][1] += 1

            heapq.heappush(q, (-self.rating_gain(productRatings[i]), i))

    @staticmethod
    def rating_gain(rating):
        a, b = rating
        return (b - a) / (b * b + b)


def fiveStartReviews(productRatings, ratingsThreshold):
    return Solution().fiveStarReviews(productRatings, ratingsThreshold)


def test_1():
    assert Solution().fiveStarReviews([[4, 4], [1, 2], [3, 6]], 77) == 3


def test_2():
    assert Solution().fiveStarReviews([[4, 4], [1, 2], [3, 6]], 99) == 241  # ???

"""

"""

