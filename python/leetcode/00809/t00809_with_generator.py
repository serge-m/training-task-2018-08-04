"""
809. Expressive Words
Medium

t=36
"""
from typing import Tuple, List


class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        END = object()

        def compress(s):
            prev = None
            cnt = 0
            for c in s:
                if prev == c:
                    cnt += 1
                else:
                    if prev is not None:
                        yield [prev, cnt]
                    prev = c
                    cnt = 1
            yield [prev, cnt]
            yield [END, 1]

        n = len(words)

        # print(list(compress(S)))
        # print([compress(w) for w in words])

        iters = [iter(compress(w)) for w in words]

        result = 0

        def match_entries(entry_s: Tuple, entry_w: Tuple):
            ch_w, cnt_w = entry_w
            ch_s, cnt_s = entry_s
            return ch_w == ch_s and (
                    (cnt_s > cnt_w and cnt_s != 2) or (cnt_s == cnt_w)
            )

        def is_final(entry):
            return entry[0] is END

        def step(entry_s):
            nonlocal result
            for i in range(n):
                if iters[i] is None:
                    continue
                entry_w = next(iters[i])
                if not match_entries(entry_s, entry_w):
                    iters[i] = None
                    continue
                if is_final(entry_s):
                    result += 1

        for entry_s in compress(S):
            step(entry_s)

        return result
