"""
1328. Break a Palindrome
Medium

t=10
s=1059
"""


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        p = palindrome
        n = len(p)
        for i in range(0, n // 2):
            if p[i] != 'a':
                return p[0:i] + 'a' + p[i + 1:]
        i = n // 2 - 1
        if i < 0:
            return ""
        return p[0:n - 1] + 'b'
