"""
253. Meeting Rooms II
Medium

t = 6

"""


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        points = []
        START = 1
        END = -1
        for start, end in intervals:
            points.append((start, START))
            points.append((end, END))

        points.sort()

        max_value = 0
        value = 0
        for t, mode in points:
            value += 1 if mode == START else -1
            max_value = max(max_value, value)
        return max_value


"""
0 0
30 1
5 0 
10 1
15 0
20 1

0 0    1
5 0    2
10 1   1 
15 0   2 
20 1   1 
30 1   0






"""
