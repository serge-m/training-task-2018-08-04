"""
981. Time Based Key-Value Store
Medium

with sortedlist
904 ms	69.7 MB
set - O(log n)
get - O(log n)
"""

from collections import deque, defaultdict
from sortedcontainers import SortedDict


class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        sd = self.map.get(key)
        if sd is None:
            return ""
        pos = sd.bisect_right(timestamp)
        if pos == 0:
            return ""
        return sd.peekitem(pos - 1)[1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
