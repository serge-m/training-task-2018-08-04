"""
777. Swap Adjacent in LR String
Medium

t=55
"""


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        def normalize(s):
            rl = []
            x = []
            for c in s:
                if c == 'X':
                    x.append(c)
                else:
                    rl.append(c)
            return rl + x

        if normalize(start) != normalize(end):
            return False

        src = list(start)
        dst = list(end)

        def bring_L(i):
            for j in range(i, n):
                if src[j] == 'R':
                    raise ValueError("matching failed")
                if src[j] == 'L':
                    src[i], src[j] = src[j], src[i]
                    return
            raise ValueError("matching failed")

        def bring_X(i):
            for j in range(i, n):
                if src[j] == 'L':
                    raise ValueError("matching failed")
                if src[j] == 'X':
                    src[i], src[j] = src[j], src[i]
                    return
            raise ValueError("matching failed")

        n = len(start)
        try:
            for i in range(n):
                if src[i] == dst[i]:
                    pass
                else:
                    if dst[i] == 'L':
                        bring_L(i)
                    elif dst[i] == 'X':
                        bring_X(i)
                    else:
                        return False
        except ValueError:
            return False
        return True


"""
XRLXXRRLX (target)
RXXLRXRXL
XRXLRXRXL

"""
