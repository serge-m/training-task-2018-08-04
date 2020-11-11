from functools import lru_cache
from typing import List
from collections import defaultdict, Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])

        mem = defaultdict(list)
        words_multiset = Counter(words)
        for word in words:
            hasher = Hasher()
            for c in word:
                hasher.add(c)
            mem[hasher.hash_value].append(word)

        hasher = Hasher()
        hashes = []
        for idx, c in enumerate(s):
            hasher.add(c)
            if idx >= word_len:
                hasher.subtract(s[idx - word_len])
            hashes.append(hasher.hash_value)
            # print(ord(c), hasher.hash_value, bin(ord(c)), bin(hasher.hash_value))

        def find(words_used, idx):
            if words_used == words_multiset:
                return True
            if idx >= len(s):
                return False

            for word in mem.get(hashes[idx], ()):
                if words_used[word] < words_multiset[word]:
                    if word != s[1 + idx - word_len:1 + idx]:
                        # print("oops")
                        pass
                    else:
                        if find(words_used + Counter([word]), idx + word_len):
                            return True

            return False

        results = []
        for idx in range(word_len - 1, len(s)):
            if find(Counter(), idx):
                results.append(idx - word_len + 1)
        return results


class Hasher:
    def __init__(self):
        self._h = 0

    def add(self, c):
        self._h = self._h ^ (ord(c) * 97)
        return self

    def subtract(self, c):
        return self.add(c)

    @property
    def hash_value(self):
        return self._h


def hash(s: str):
    pass


def test_1():
    result = Solution().findSubstring(s="barfoothefoobarman", words=["foo", "bar"])
    assert result == [0, 9]


def test_2():
    result = Solution().findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"])
    assert result == []


def test_3():
    result = Solution().findSubstring(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"])
    assert result == [6, 9, 12]
