""" Tests suite for the module stack.py"""
import pytest
from stack import Stack


@pytest.fixture
def empty_stack():
    return Stack()


@pytest.fixture
def filled_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    return stack


def test_push(empty_stack):
    empty_stack.push(5)
    assert empty_stack.peek() == 5


def test_pop(filled_stack):
    assert filled_stack.pop() == 4
    assert filled_stack.peek() == 3


def test_peek(filled_stack):
    assert filled_stack.peek() == 4


def test_print_stack(capsys, filled_stack):
    filled_stack.print_stack()
    captured = capsys.readouterr()
    assert captured.out.strip() == '|4|\n|3|\n|2|\n|1|'


def test_pop_from_empty(empty_stack):
    with pytest.raises(Exception):
        empty_stack.pop()


def test_peek_from_empty(empty_stack):
    with pytest.raises(Exception):
        empty_stack.peek()


if __name__ == "__main__":
    pytest.main([__file__])
    