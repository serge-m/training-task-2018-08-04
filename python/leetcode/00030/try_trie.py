from dataclasses import dataclass
from typing import Dict

import pytest


@dataclass
class TrieNode:
    next: Dict
    count: int = 0


class TrieKeyNotFound(Exception):
    pass


class Trie:
    def __init__(self):
        self._root = TrieNode({}, 0)

    def add(self, word):
        cursor = self._root
        for c in word:
            cursor = self._root.next.setdefault(c, TrieNode({}, 0))

        cursor.count += 1

    def find(self, word):
        cursor = self._root
        try:
            for c in word:
                cursor = self._root.next[c]
        except KeyError:
            raise TrieKeyNotFound(word)
        return cursor


def test_trie():
    t = Trie()
    with pytest.raises(TrieKeyNotFound):
        t.find("bar")
    t.add("bar")
    assert t.find("bar").count == 1
    assert t.find("ba").count == 0
    t.add("baz")
    assert t.find("bar").count == 1
    assert t.find("baz").count == 1
    assert t.find("ba").count == 0
    t.add("foo")
    assert t.find("foo").count == 1
    assert t.find("bar").count == 1
    assert t.find("baz").count == 1
    assert t.find("ba").count == 0
    t.add("baz")
    assert t.find("bar").count == 1
    assert t.find("baz").count == 2
    assert t.find("ba").count == 0
