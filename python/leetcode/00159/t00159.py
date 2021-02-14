"""
159. Longest Substring with At Most Two Distinct Characters
Medium

"""


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s:
            return 0
        start_latest_group = deque([0])
        ts = [s[0]]
        c = 1
        maxc = 1
        # print(c, start_latest_group)
        for i in range(1, len(s)):
            if (s[i] == s[start_latest_group[0]] or s[i] == s[start_latest_group[-1]]):
                c += 1
            else:
                c = i - start_latest_group[-1] + 1

            if s[i] != s[i - 1]:
                start_latest_group.append(i)

            if len(start_latest_group) > 2:
                start_latest_group.popleft()

                # print(i, c, start_latest_group)
            maxc = max(maxc, c)
        return maxc


