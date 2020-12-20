#!/bin/python3

import os
import sys


#
# Complete the contacts function below.
#
def contacts(queries):
    trie = Trie()
    result = []
    for cmd, word in queries:

        if cmd == 'add':
            trie.add(word)
        elif cmd == 'find':
            result.append(trie.find(word))
        else:
            raise ValueError('unknown command')
    return result


def make_empty():
    return {
        'sum': 0,
        'next': {}
    }


class Trie:
    def __init__(self):
        self.root = make_empty()

    def add(self, word):
        cur = self.root
        for c in word:
            cur['sum'] += 1
            cur_next = cur['next']
            cur = cur_next.setdefault(c, make_empty())
        cur['sum'] += 1

    def find(self, word):
        cur = self.root
        for c in word:
            cur = cur.get('next', {}).get(c)
            if cur is None:
                return 0

        return cur['sum']


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
