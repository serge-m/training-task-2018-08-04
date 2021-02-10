"""
853. Car Fleet
Medium

O(n**2), can be better
"""


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        if n < 2:
            return n
        p_s = sorted([(p, s) for p, s in zip(position, speed)])

        POS = 0
        SPEED = 1
        """
        t = (x0[i+1] - x0[i]) / (v[i] - v[i+1])
        x = x0[i] + v[i] * t = x0[i] + v[i] * (x0[i+1] - x0[i]) / (v[i] - v[i+1]) =
        = (v[i]*x0[i] - v[i+1] * x0[i] + v[i] * x0[i+1] - v[i] * x0[i]) / (v[i] - v[i+1])=
        (v[i] * x0[i+1]  - v[i+1] * x0[i] ) / (v[i] - v[i+1])
        """

        x0 = [ps[POS] for ps in p_s]
        v = [ps[SPEED] for ps in p_s]
        merges = 0
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if v[i] < v[j]:
                    continue
                if v[i] == v[j]:
                    if x0[i] == x0[j]:
                        merges += 1
                        break
                    else:
                        continue
                xc = (v[i] * x0[j] - v[j] * x0[i]) / (v[i] - v[j])
                if xc <= target:
                    merges += 1
                    break
        return n - merges

