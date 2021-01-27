"""
460. LFU Cache
Hard

t=55

Slow operations. TODO: introduce double linked lists in Usage to usage updates O(1)
"""
from collections import deque, defaultdict


class ValCnt:
    def __init__(self, val, cnt):
        self.val = val
        self.cnt = cnt


class LFUCache:

    def __init__(self, capacity: int):
        self.k2v = dict()
        self.usage = Usage()
        self.capacity = capacity

    def get(self, key: int) -> int:
        # print(f"get key {key} self.k2v {self.k2v} self.usage {self.usage}" )
        v = self.k2v.get(key)
        if v is None:
            return -1
        if self.capacity != 0:
            self.usage.increment_usage(key)
        return v

    def put(self, key: int, value: int) -> None:
        # print(f"put key {key} value {value} self.k2v {self.k2v} self.usage {self.usage}" )
        if key not in self.k2v:
            if self.capacity == 0:
                return
            # insert
            if self.full():
                k_del = self.usage.delete()
                del self.k2v[k_del]

            self.k2v[key] = value
            self.usage.add(key)
            return
        # update
        self.k2v[key] = value
        self.usage.increment_usage(key)

    def full(self):
        return len(self.k2v) == self.capacity


class Usage:
    def __init__(self):

        self.k2cnt = dict()
        self.cnt2usage = dict()

    def increment_usage(self, key):
        cnt = self.k2cnt[key]
        self.cnt2usage[cnt].remove(key)
        if not self.cnt2usage[cnt]:
            del self.cnt2usage[cnt]
        self.cnt2usage.setdefault(cnt + 1, deque()).append(key)
        self.k2cnt[key] += 1

    def delete(self):
        min_cnt = min(self.cnt2usage.keys())
        key_to_delete = self.cnt2usage[min_cnt].popleft()
        if not self.cnt2usage[min_cnt]:
            del self.cnt2usage[min_cnt]
        del self.k2cnt[key_to_delete]
        return key_to_delete

    def add(self, key):
        self.k2cnt[key] = 1
        self.cnt2usage.setdefault(1, deque()).append(key)

    def __str__(self):
        return f"self.k2cnt {self.k2cnt} self.cnt2usage {self.cnt2usage}"

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
