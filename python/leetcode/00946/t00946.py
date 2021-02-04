"""
946. Validate Stack Sequences
Medium

t=20
"""


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        stack = []
        i_pu = 0
        for po in popped:
            while len(stack) == 0 or stack[-1] != po:
                if i_pu == n:
                    return False
                stack.append(pushed[i_pu])
                i_pu += 1

            stack.pop()

        return len(stack) == 0


"""

i  0 1 2 3 4
pu 1 2 3 4 5

i_pu = 5
po = 
stack 
"""
