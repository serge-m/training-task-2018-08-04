"""
981. Time Based Key-Value Store
Medium

664 ms	70.4 MB

"""

from collections import deque, defaultdict
import bisect


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.map.get(key)
        if lst is None:
            return ""
        pos = bisect.bisect_left(lst, (timestamp + 1, ""))
        if pos == 0:
            return ""
        return lst[pos - 1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
