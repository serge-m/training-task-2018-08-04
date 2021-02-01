"""
146. LRU Cache
Medium

t = 41
"""

from typing import Dict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # head is recent, tail is old
        self.to_head = Node(None, None)
        self.to_tail = Node(None, None)

        self.to_head.older = self.to_tail
        self.to_tail.newer = self.to_head

        self.k2node: Dict[int, Node] = dict()

    def get(self, key: int) -> int:
        node = self.k2node.get(key)
        if node is None:
            return -1
        self._delete_existing_node(node)
        self._add_new_node(key, node.value)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.k2node:
            self._delete(key)
        elif len(self.k2node) >= self.capacity:
            self._evict()

        self._add_new_node(key, value)

    def _add_new_node(self, key, value):
        node = Node(key, value)
        node.older = self.to_head.older
        node.newer = self.to_head
        self.to_head.older.newer = node
        self.to_head.older = node
        self.k2node[key] = node

    def _delete_existing_node(self, node):
        del self.k2node[node.key]
        newer, older = node.newer, node.older
        newer.older = older
        older.newer = newer
        node.newer = node.older = None

    def _delete(self, key):
        self._delete_existing_node(self.k2node[key])

    def _evict(self):
        self._delete_existing_node(self.to_tail.newer)


class Node:
    def __init__(self, key, value):
        self.older = None
        self.newer = None
        self.value = value
        self.key = key


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

def main():
    from tqdm import tqdm
    capacity = 3
    obj = LRUCache(capacity)
    for i in tqdm(range(10000000)):
        z = obj.get(1)
        obj.put(1, 10)
        obj.put(2, 20)
        z = obj.get(1)
        obj.put(3, 30)
        obj.put(4, 40)


# if __name__ == '__main__':
#     main()
