"""Test suites for module binary_search_tree.py"""
import pytest

from binary_search_tree import BinarySearchTree


@pytest.fixture
def empty_bst():
    return BinarySearchTree()


@pytest.fixture
def filled_bst():
    bst = BinarySearchTree()
    for key in (9, 5, 8, 6, 7):
        bst.insert(key)
    return bst


def test_insert(empty_bst):
    empty_bst.insert(3)
    empty_bst.insert(1)
    empty_bst.insert(0)
    empty_bst.insert(2)
    empty_bst.insert(4)
    assert empty_bst.inorder_traversal() == "0 1 2 3 4"


def test_lookup(filled_bst):
    assert filled_bst.lookup(7).key == 7


def test_delete(filled_bst):
    filled_bst.delete(6)
    assert filled_bst.inorder_traversal() == "5 7 8 9"


if __name__ == "__main__":
    pytest.main([__file__])
    