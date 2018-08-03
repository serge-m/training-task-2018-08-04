import pytest

from brackets.brackets_sequence import is_valid_string

"""
Tests for bracket_sequence
pytest is required
"""


def test_empty():
    assert not is_valid_string('')


def test_simplest_correct():
    assert is_valid_string('()')
    assert is_valid_string('[]')
    assert is_valid_string('{}')


def test_unclosed_single_brackets():
    assert not is_valid_string('(')
    assert not is_valid_string('[')
    assert not is_valid_string('{')

    assert not is_valid_string(')')
    assert not is_valid_string(']')
    assert not is_valid_string('}')


def test_nested():
    assert is_valid_string('(()[]{})')
    assert not is_valid_string('((})')


def test_valid_examples_from_the_task():
    assert is_valid_string("{[]()}")
    assert is_valid_string("(){}")
    assert is_valid_string("[(){}]")


def test_invalid_examples_from_the_task():
    assert not is_valid_string("{)")
    assert not is_valid_string("{)(}")


def test_invalid_with_correct_amount():
    assert not is_valid_string("[(])")
    assert not is_valid_string("[({}])")


def test_long_string_with_pattern():
    input_string = "{()[]}" * 10000
    assert is_valid_string(input_string)


def test_long_string_with_enclosing():
    input_string = "(" + "{()[]}" * 10000 + ")"
    assert is_valid_string(input_string)


def test_deep_nested():
    input_string = "({[" * 10000 + "{}" * 2000 + "]})" * 10000
    assert is_valid_string(input_string)


def test_incorrect_symbols():
    with pytest.raises(Exception):
        is_valid_string("a")

    with pytest.raises(Exception):
        is_valid_string("(b)")
