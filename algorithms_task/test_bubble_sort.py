"""Tests suites for bubble_sort.py module"""

import pytest

from bubble_sort import bubble_sort


@pytest.mark.parametrize("arr, is_descending, expected_result", [
    ([22, 96, 2, 1, 2, 67, 68, 25, 17, 5, 31], False, [1, 2, 2, 5, 17, 22, 25, 31, 67, 68, 96]),
    ([22, 96, 2, 1, 2, 67, 68, 25, 17, 5, 31], True, [96, 68, 67, 31, 25, 22, 17, 5, 2, 2, 1]),
    ([100000, 123, 129450, -193, 972, -59, 3], False, [-193, -59, 3, 123, 972, 100000, 129450]),
    ([100000, 123, 129450, -193, 972, -59, 3], True, [129450, 100000, 972, 123, 3, -59, -193]),
    ([-23, 98, 0, -3, -5, 145, 2.5], False, [-23, -5, -3, 0, 2.5, 98, 145]),
    ([-23, 98, 0, -3, -5, 145, 2.5], True, [145, 98, 2.5, 0, -3, -5, -23]),
    ({5, 0, 4, 3, 2, 1}, False, [0, 1, 2, 3, 4, 5]),
    ({5, 0, 4, 3, 2, 1}, True, [5, 4, 3, 2, 1, 0]),
    ((5, 0, 4, 3, 2, 1), False, [0, 1, 2, 3, 4, 5]),
    ((5, 0, 4, 3, 2, 1), True, [5, 4, 3, 2, 1, 0])
])
def test_bubble_sort(arr, is_descending, expected_result):
    assert bubble_sort(arr, is_descending) == expected_result


if __name__ == "__main__":
    pytest.main([__file__])
