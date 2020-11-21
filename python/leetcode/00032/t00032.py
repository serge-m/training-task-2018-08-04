class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [['^', 0]]  # stack contains tuples (char, count)
        len_longest = 0

        for c in s:
            if c == '(':
                stack.append([c, 0])
            else:  # c == ')'
                last = stack[-1]
                if last[0] == '(':
                    stack.pop()
                    stack[-1][1] += last[1] + 2
                    len_longest = max(len_longest, stack[-1][1])
                else:
                    stack.append([c, 0])

        return len_longest


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
    assert s.longestValidParentheses("(()(())") == 6
    assert s.longestValidParentheses("(()((())") == 4
    assert s.longestValidParentheses("(())(())") == 8
    assert s.longestValidParentheses("(()))(())") == 4
    assert s.longestValidParentheses("(())((())") == 4


def test_4():
    s = Solution()
    assert s.longestValidParentheses(")()())()()(") == 4
