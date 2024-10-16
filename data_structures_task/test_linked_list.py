""" Tests suite for the module linked_list.py"""

import pytest

from linked_list import LinkedList


@pytest.fixture
def empty_linked_list():
    return LinkedList()


@pytest.fixture
def filled_linked_list():
    linked_list = LinkedList()
    linked_list.prepend(7)
    linked_list.append(3)
    linked_list.prepend(70)
    linked_list.append(30)
    linked_list.insert(77, 2)
    return linked_list


def test_prepend(empty_linked_list):
    empty_linked_list.prepend(5)
    assert empty_linked_list.get_len() == 1
    assert empty_linked_list.lookup(5) == 0


def test_append(empty_linked_list):
    empty_linked_list.append(10)
    assert empty_linked_list.get_len() == 1
    assert empty_linked_list.lookup(10) == 0


def test_insert(filled_linked_list):
    filled_linked_list.insert(50, 2)
    assert filled_linked_list.get_len() == 6
    assert filled_linked_list.lookup(50) == 2


def test_delete(filled_linked_list):
    filled_linked_list.delete(1)
    assert filled_linked_list.get_len() == 4
    assert filled_linked_list.lookup(7) == -1


def test_lookup(filled_linked_list):
    assert filled_linked_list.lookup(70) == 0
    assert filled_linked_list.lookup(30) == 4
    assert filled_linked_list.lookup(100) == -1


def test_empty_linked_list_print(capsys, empty_linked_list):
    empty_linked_list.print_linked_list()
    captured = capsys.readouterr()
    assert captured.out.strip() == 'empty linked list'


def test_filled_linked_list_print(capsys, filled_linked_list):
    filled_linked_list.print_linked_list()
    captured = capsys.readouterr()
    assert captured.out.strip() == '|70| --> |7| --> |77| --> |3| --> |30|'


if __name__ == "__main__":
    pytest.main([__file__])
    