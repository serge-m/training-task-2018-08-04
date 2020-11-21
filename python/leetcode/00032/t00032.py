class Solution:
    def longestValidParentheses(self, s: str) -> int:
        all_counts = []
        stack = []
        cnt = 0
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if not stack:
                    all_counts.append(cnt)
                    cnt = 0
                else:
                    prev = stack.pop()
                    if prev == '(':
                        cnt += 2
                    else:
                        raise ValueError("unexpected value")
            else:
                raise ValueError("bad character")
        all_counts.append(cnt)
        return max(all_counts, default=0)


def test_1():
    s = Solution()
    assert s.longestValidParentheses("(()") == 2
    assert s.longestValidParentheses(")()())") == 4
    assert s.longestValidParentheses("") == 0


def test_2():
    s = Solution()
    assert s.longestValidParentheses("()(()") == 2


def test_3():
    s = Solution()
    assert s.longestValidParentheses("()())()") == 4


"""
0
(

 0
((

1
(



()())()

0
(

2


2
(

4
_

40
x

4
(
"""
