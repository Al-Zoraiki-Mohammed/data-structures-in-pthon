""" Tests suite for the module my_queue.py"""
import pytest
from my_queue import Queue


@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def filled_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    return queue


def test_enqueue(empty_queue):
    empty_queue.enqueue(5)
    assert empty_queue.peek() == 5


def test_dequeue(filled_queue):
    assert filled_queue.dequeue() == 1
    assert filled_queue.peek() == 2


def test_peek(filled_queue):
    assert filled_queue.peek() == 1


def test_print_queue(capsys, filled_queue):
    filled_queue.print_queue()
    captured = capsys.readouterr()
    assert captured.out.strip() == '|4| |3| |2| |1|'


def test_dequeue_from_empty(empty_queue):
    with pytest.raises(Exception):
        empty_queue.dequeue()


def test_peek_from_empty(empty_queue):
    with pytest.raises(Exception):
        empty_queue.peek()


if __name__ == "__main__":
    pytest.main([__file__])
    