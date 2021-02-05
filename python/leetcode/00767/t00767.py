"""
767. Reorganize String
Medium

"""

from collections import Counter


class Solution:
    def reorganizeString(self, S: str) -> str:
        if not S:
            return ""
        cnt = Counter(S)
        result = []
        while len(result) < len(S):
            c1, cnt1 = cnt.most_common(1)[0]
            del cnt[c1]
            for i in range(cnt1):
                result.append(c1)
                if not cnt:
                    if i == cnt1 - 1:
                        break
                    else:
                        return ""
                c2, cnt2 = cnt.most_common(1)[0]
                result.append(c2)
                cnt[c2] -= 1
                if cnt[c2] == 0:
                    del cnt[c2]
                # print(result, cnt)
        return ''.join(result)

