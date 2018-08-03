#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def is_valid_string(string: str) -> bool:
    """
    Assumptions:
    * the string may contain only brackets => If the string contains other characters the exception is thrown.
    * Empty string is invalid. The grammar doesn't include the empty string.
    * Input type is a string. Behavior on the other types of inputs is not supported/tested.

    :param string: string of characters, which consist of opened and closed parentheses (‘{‘, ‘(‘, ‘[‘, )
    :return: True if the string is valid brackets sequence
    """
    if string == "":
        return False
    stack = []
    for char in string:
        if char in ['(', '[', '{']:
            stack.append(char)
        elif char in [')', ']', '}']:
            if not _pop_from_stack_and_check(stack, char):
                return False
        else:
            raise Exception("Invalid input. Only brackets characters are allowed.")
    return len(stack) == 0


def _pop_from_stack_and_check(stack, char):
    try:
        top = stack.pop()
    except IndexError:
        return False

    return _is_matching(top, char)


def _is_matching(start_char, end_char):
    pair = (start_char, end_char)
    return pair == ('(', ')') or \
           pair == ('[', ']') or \
           pair == ('{', '}')


if __name__ == '__main__':
    import sys
    try:
        string = sys.argv[1]
    except IndexError:
        print('Usage: {command} "<BRACKETS_SEQUENCE>"\n'
              '  Example: {command} "[()]"' .format(command=sys.argv[0]))
        exit(1)

    try:
        print(is_valid_string(string))
    except Exception as e:
        print("Failure: {}".format(e))
        exit(1)

