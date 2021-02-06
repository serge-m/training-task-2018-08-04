"""
809. Expressive Words
Medium

t=36
"""


class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def compress(s):
            result = []
            for c in s:
                if result and result[-1][0] == c:
                    result[-1][1] += 1
                else:
                    result.append([c, 1])
            result.append(("end", 0))
            return result

        n = len(words)

        # print(compress(S))
        # print([compress(w) for w in words])

        iters = [iter(compress(w)) for w in words]

        result = 0

        def step(ch_s, cnt_s):
            nonlocal result
            for i in range(n):
                if iters[i] is None:
                    continue
                ch_w, cnt_w = next(iters[i], (None, 0))
                if ch_w == ch_s and (
                        (cnt_s > cnt_w and cnt_s != 2) or (cnt_s == cnt_w)
                ):
                    if ch_w == 'end':
                        result += 1
                        iters[i] = None
                else:
                    iters[i] = None

        for ch_s, cnt_s in compress(S):
            step(ch_s, cnt_s)

        return result
