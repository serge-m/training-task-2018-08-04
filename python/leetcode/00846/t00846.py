"""
846. Hand of Straights
Medium


"""


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        cnts = defaultdict(int)
        for c in hand:
            cnts[c] += 1
        unique = sorted(cnts.keys())

        i_u = 0

        def get_start():
            nonlocal i_u
            while i_u < len(unique):
                c = unique[i_u]
                if cnts[c] > 0:
                    return c
                i_u += 1
            return None

        def get_seq():
            start = get_start()
            if start is None:
                return False
            c = start
            for i in range(W):
                cnts[c] -= 1
                if cnts[c] < 0:
                    return False
                c += 1
            return True

        processed = 0
        while True:
            if not get_seq():
                return False
            processed += W
            if processed == len(hand):
                return True



