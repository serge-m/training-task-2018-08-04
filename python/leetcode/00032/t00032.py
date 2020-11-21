from dataclasses import dataclass


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [StackItem('^', 0)]

        for c in s:
            if c == '(':
                stack.append(StackItem(c, 0))
            else:  # c == ')'
                last: StackItem = stack[-1]
                if last.char == '(':
                    stack.pop()
                    stack[-1].cnt += last.cnt + 2
                else:
                    stack.append(StackItem(c, 0))

        return max((i.cnt for i in stack), default=0)


@dataclass
class StackItem:
    char: str
    cnt: int


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
