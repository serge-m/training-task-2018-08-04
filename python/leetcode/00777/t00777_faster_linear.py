"""
777. Swap Adjacent in LR String
Medium

t=60
"""


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        src = list(start)
        dst = list(end)

        next_src_L = 0
        next_src_X = 0

        def bring_L(i):
            nonlocal next_src_L
            i_start = max(i, next_src_L)
            for j in range(i_start, n):
                if src[j] == 'R':
                    raise ValueError("matching failed")
                if src[j] == 'L':
                    src[i], src[j] = src[j], src[i]
                    next_src_L = j
                    return
            raise ValueError("matching failed")

        def bring_X(i):
            nonlocal next_src_X
            i_start = max(i, next_src_X)
            for j in range(i_start, n):
                if src[j] == 'L':
                    raise ValueError("matching failed")
                if src[j] == 'X':
                    src[i], src[j] = src[j], src[i]
                    next_src_X = j
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
