#!/bin/python3
import os


def isBalanced(s) -> str:
    matching = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    stack = []
    for c in s:
        if c in ('(', '{', '['):
            stack.append(c)
            continue
        else:
            try:
                if stack.pop() == matching[c]:
                    continue
            except IndexError:
                pass
            return 'NO'
    if stack:
        return 'NO'
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        fptr.write(result + '\n')
    fptr.close()
