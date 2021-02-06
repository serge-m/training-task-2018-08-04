from collections import Counter, defaultdict
from dataclasses import dataclass, field


def node_gen():
    return Node()


@dataclass
class Node:
    count: int = 0
    nxt: defaultdict = field(default_factory=node_gen)


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, w):
        node = self.root
        for c in w:
            node = node.nxt[c]
        node.count += 1


