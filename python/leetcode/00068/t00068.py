"""
68. Text Justification
Hard

t=50

"""
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        if not words:
            return []
        len_line = len(words[0])
        id_start = 0
        for id_cur in range(1, len(words)):
            word = words[id_cur]
            new_len_line = len_line + 1 + len(word)
            if new_len_line <= maxWidth:
                # add word with 1 space to current string
                len_line = new_len_line
            else:
                # produce a new line
                result.append(build_line(words[id_start:id_cur], maxWidth))
                len_line = len(word)
                id_start = id_cur

        if len_line != 0:
            line = ' '.join(words[id_start:])
            line = line + ' ' * (maxWidth - len(line))
            result.append(line)

        return result


def build_line(words, maxWidth):
    num_words = len(words)
    sum_len = sum(len(w) for w in words)
    sum_spaces = (maxWidth - sum_len)
    if num_words == 1:
        return words[0] + " " * sum_spaces

    num_gaps = num_words - 1

    ordinary_spaces = sum_spaces // num_gaps
    extended_spaces = sum_spaces % num_gaps
    lst = [words[0]]
    for w in words[1:]:
        len_delim = ordinary_spaces
        if extended_spaces > 0:
            len_delim += 1
            extended_spaces -= 1
        lst.append(" " * len_delim)
        lst.append(w)

    return "".join(lst)





