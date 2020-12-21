class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        table = [
            [0 for _ in range(n2 + 1)]
            for _ in range(n1 + 1)
        ]

        i1 = 0
        for i2 in range(0, n2 + 1):
            table[i1][i2] = i2

        for i1 in range(1, n1 + 1):
            table[i1][0] = i1

            for i2 in range(1, n2 + 1):
                if word1[i1 - 1] == word2[i2 - 1]:
                    table[i1][i2] = table[i1 - 1][i2 - 1]
                else:
                    table[i1][i2] = min(
                        table[i1 - 1][i2 - 1] + 1,
                        table[i1 - 1][i2] + 1,
                        table[i1][i2 - 1] + 1,
                    )
        return table[n1][n2]


"""
w1 abc
w2 c

ab 
null


abce
cd

abc
c

abc
cd

abce
c


rose
ros


rorse
rose

horse
rorse
"""
