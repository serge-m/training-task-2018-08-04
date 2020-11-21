import copy
from collections import defaultdict, Counter
from typing import List, Dict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        len_word = len(words[0])
        return sum(
            (
                [
                    found + start
                    for found in find(s[start:], words)
                ]
                for start in range(0, len_word)
            ),
            []
        )


class Matcher:
    """
    Matches a sliding window of integer sequence to a given multiset of integers.
    Multiset is represented as dictionary with counts.
    Sliding window is represented as `add` and `remove` operations that have to be applied
    by the user as the window moves along the sequence.
    """
    def __init__(self, target_counts: Dict[int, int]):
        self.target_counts = target_counts
        self.target_sum = sum(self.target_counts.values())
        self.current_counts = defaultdict(int)
        self.current_sum = 0

    def add(self, word: int):
        self.current_counts[word] += 1
        self.current_sum += 1

    def remove(self, word: int):
        self.current_counts[word] -= 1
        self.current_sum -= 1

    def full(self):
        if sum(self.current_counts.values()) != self.target_sum:
            return False

        for word, cnt in self.target_counts.items():
            if self.current_counts[word] != cnt:
                return False

        return True


def find(s: str, words: List[str]):
    cnt_words = len(words)
    len_word = len(words[0])  # assuming all the words are of the same length
    word_to_id, id_counts = build_word_counts(words)  # can be extracted to a caller.

    sequence = [
        word_to_id.get(s[pos: pos + len_word], -1)
        for pos in range(0, len(s), len_word)
    ]

    found = match_int_sequence(sequence, id_counts, cnt_words)

    return [pos * len_word for pos in found]


def match_int_sequence(sequence, target_counts, cnt_words):
    matcher = Matcher(target_counts)

    result = []
    for pos in range(len(sequence)):
        matcher.add(sequence[pos])
        pos_to_remove = pos - cnt_words
        if pos_to_remove >= 0:
            matcher.remove(sequence[pos_to_remove])
        if matcher.full():
            result.append(pos - cnt_words + 1)

    return result


def build_word_counts(words):
    word_to_id = {}
    id_counts = {}
    for word_id, word in enumerate(words):
        if word not in word_to_id:
            word_to_id[word] = word_id
            id_counts[word_id] = 1
        else:
            id_counts[word_to_id[word]] += 1

    return word_to_id, id_counts


def test_find():
    assert find("b.a.a.a.b.a.a.b.a.", ["a.", "a.", "b.", "b."]) == [8]


def test_1():
    result = Solution().findSubstring(s="barfoothefoobarman", words=["foo", "bar"])
    assert result == [0, 9]


def test_2():
    result = Solution().findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"])
    assert result == []


def test_3():
    result = Solution().findSubstring(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"])
    assert result == [6, 9, 12]
