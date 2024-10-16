"""Test suite for binary_search.py module"""

import pytest

from binary_search import binary_search


@pytest.mark.parametrize("arr, key, is_sorted, expected_result", [
    ([10, 20, 30, 40, 50], 20, True, 1),
    ([10, 20, 30, 40, 50], 200, True, -1),
    ([50, 20, 10, 40, 30], 50, False, 4),
    ((50, 20, 10, 40, 30), 10, False, 0),
    ({50, 20, 10, 40, 30}, 40, False, 3),
    ({'banana', 'apple', 'pear'}, 'apple', False, 0),
    ({'banana', 'apple', 'pear'}, 'orange', False, -1)

])
def test_binary_search(arr, key, is_sorted, expected_result):
    assert binary_search(arr, key, is_sorted) == expected_result


if __name__ == "__main__":
    pytest.main([__file__])
