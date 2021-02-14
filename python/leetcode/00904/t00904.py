"""
904. Fruit Into Baskets
Medium

"""

from collections import Counter


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        begin = {tree[0]: 0}
        maxcnt = 1
        c = 1
        for i in range(1, len(tree)):
            if tree[i] in begin:
                if tree[i] == tree[i - 1]:
                    pass
                else:
                    begin[tree[i]] = i
                c += 1
            else:
                if len(begin) < 2:
                    begin[tree[i]] = i
                    c += 1
                else:
                    begin = {
                        tree[i - 1]: begin[tree[i - 1]],
                        tree[i]: i
                    }
                    c = i - begin[tree[i - 1]] + 1
            maxcnt = max(maxcnt, c)

        return maxcnt
