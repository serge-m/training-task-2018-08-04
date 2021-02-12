"""
149. Max Points on a Line
Hard

O(n^2*log n)
"""


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # print(on_the_line([0, 0], [1, 2], [0, 1]))
        # print(on_the_line([0, 0], [1, 2], [-1, -2]))
        # print(on_the_line([3, 4], [4, 5], [1, 1]))

        n = len(points)
        if n < 3:
            return n
        best = 0

        # dups = Counter(map(tuple, points))
        # best = dups.most_common(1)[0][1]
        # print(best)

        for i in range(n):
            # print(i, points[i], ":")
            # print("best", best)
            angles_points = [
                (compute_angle(points[i], points[j]), points[j])
                for j in range(n)
                if points[i] != points[j]
            ]
            la = len(angles_points)
            num_duplicates = n - la

            if la < 2:
                best = max(best, n - la)
                continue
            angles_points.sort()
            # print("num duplicates", num_duplicates)
            # print(angles_points)
            # print("best", best)
            prev_j = 0
            c = 1
            for j in range(1, len(angles_points)):
                if on_the_line(points[i], angles_points[prev_j][1], angles_points[j][1]):
                    c += 1
                else:
                    prev_j = j
                    c = 1
                best = max(best, c + num_duplicates)
            # print("best after", best)

        return best


X = 0
Y = 1


def compute_angle(p1, p2):
    return math.atan2(p2[Y] - p1[Y], p2[X] - p1[X])


def on_the_line(p1, p2, p):
    top1 = (p[X] - p1[X])
    bot1 = (p[Y] - p1[Y])
    top2 = (p1[X] - p2[X])
    bot2 = (p1[Y] - p2[Y])
    return top1 * bot2 - top2 * bot1 == 0
