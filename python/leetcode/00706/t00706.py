"""
706. Design HashMap
Easy
"""

DELETED = object()


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        initial_size = 4
        self.a = [None] * initial_size
        self.len = 0

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        # print(f"put {key} {value} start", self.a)
        if not _add(self.a, key, value):
            pass
        else:
            self.len += 1
            if self.len > len(self.a) * 0.6:
                self.a = _rehash(self.a)
        # print(f"put {key} {value}  end", self.a)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        for i in probe_seq(hash(key), len(self.a)):
            if self.a[i] is None:
                return -1
            if self.a[i] is DELETED:
                continue
            k, v = self.a[i]
            if k == key:
                return v
            else:
                continue

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        # print(f"remove {key} start", self.a)
        for i in probe_seq(hash(key), len(self.a)):
            if self.a[i] is None:
                break
            if self.a[i] is DELETED:
                continue
            k, v = self.a[i]
            if k == key:
                self.a[i] = DELETED
                self.len -= 1
                break
            else:
                continue
        # print(f"remove {key}   end", self.a)


def _rehash(a):
    new_a = [None] * (len(a) * 2)
    for entry in a:
        if entry is None or entry is DELETED:
            continue
        k, v = entry
        _add(new_a, k, v)
    return new_a


def p(attempt):
    return attempt * 97


def probe_seq(start, size):
    attempt = 0
    while True:
        yield (start + p(attempt)) % size
        attempt += 1


def _add(a, key, value):
    for i in probe_seq(hash(key), len(a)):
        if a[i] is None or a[i] is DELETED:
            a[i] = (key, value)
            return True
        k, v = a[i]
        if k == key:
            a[i] = (key, value)
            return False


def test_probe_seq():
    key = 123123
    for array_len in [20, 32, 1024]:
        seq = [
            v
            for i, v in zip(range(array_len), probe_seq(hash(key), array_len))
        ]
        probed = sorted(seq)
        assert probed == list(range(array_len))


def test_standard_hash():
    for i in range(1000000):
        if i != hash(i):
            print(i, hash(i))
            break

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
