from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        with_key = [
            (self.make_key(log, idx), log) for idx, log in enumerate(logs)
        ]
        with_key.sort()
        return [log for key, log in with_key]

    @staticmethod
    def make_key(log, idx):
        words = log.split(' ')
        first_word = words[1]
        if first_word[0].isdecimal():
            return 1, idx
        else:
            return 0, words[1:], words[0]


def test_1():
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    result = Solution().reorderLogFiles(logs)
    assert result == ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
