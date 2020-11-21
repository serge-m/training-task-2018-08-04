import copy
from collections import defaultdict, Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        len_word = len(words[0])
        return sum(
            [
                [
                    found + start
                    for found in find(s[start:], words)
                ]
                for start in range(0, len_word)
            ],
            []
        )


class Matcher:
    def __init__(self, id_counts):
        self.id_counts = id_counts
        self.current_counts = defaultdict(int)

    def add(self, word_id):
        self.current_counts[word_id] += 1

    def remove(self, word_id):
        self.current_counts[word_id] -= 1

    def full(self):
        if sum(self.current_counts.values()) != sum(self.id_counts.values()):
            return False

        for word_id, cnt in self.id_counts.items():
            if self.current_counts[word_id] != cnt:
                return False

        return True


def find(s: str, words: List[str]):
    len_word = len(words[0])
    word_to_id, id_counts = build_word_counts(words)

    translated = [
        word_to_id.get(s[pos: pos + len_word], -1)
        for pos in range(0, len(s), len_word)
    ]

    matcher = Matcher(id_counts)

    result = []
    for pos in range(len(translated)):
        matcher.add(translated[pos])
        pos_to_remove = pos - len(words)
        if pos_to_remove >= 0:
            matcher.remove(translated[pos_to_remove])
        if matcher.full():
            result.append((pos - len(words) + 1) * len_word)

    return result


def build_word_counts(words):
    word_to_id = {}
    id_counts = {}
    word_count = {}
    for word_id, word in enumerate(words):
        if word not in word_to_id:
            word_to_id[word] = word_id
            word_count[word] = 1
            id_counts[word_id] = 1
        else:
            word_count[word] += 1
            id_counts[word_to_id[word]] += 1

    return word_to_id, id_counts


def test_find():
    assert find("b.a.a.a.b.a.a.b.a.", ["a.", "a.", "b.", "b."]) == [8]


def test_counter():
    s = Counter(['a', 'b', 'a'])
    s.subtract('a')
    assert s == Counter(['a', 'b'])
    s.subtract('a')
    assert s == Counter({'b': 1, 'a': 0})


def test_1():
    result = Solution().findSubstring(s="barfoothefoobarman", words=["foo", "bar"])
    assert result == [0, 9]


def test_2():
    result = Solution().findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"])
    assert result == []


def test_3():
    result = Solution().findSubstring(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"])
    assert result == [6, 9, 12]
