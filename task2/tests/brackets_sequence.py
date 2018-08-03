from task2.brackets_sequence import is_valid_string

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

def test_invalid_examples_from_the_task():
    assert not is_valid_string("{)")
    assert not is_valid_string("{)(}")
