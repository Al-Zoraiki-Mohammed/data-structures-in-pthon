"""Test recursive_factorial.py"""

import pytest

from recursive_factorial import factorial


@pytest.mark.parametrize("num, expected_result", [
    (5, 120),
    (1, 1),
    (0, 1)
])
def test_factorial(num, expected_result):
    assert factorial(num) == expected_result


def test_factorial_negative():
    with pytest.raises(Exception) as exc_info:
        factorial(-5)
    assert str(exc_info.value) == "Type Error: number must be positive integer"


def test_factorial_float():
    with pytest.raises(Exception) as exc_info:
        factorial(5.5)
    assert str(exc_info.value) == "Type Error: number must be positive integer"


def test_factorial_string():
    with pytest.raises(Exception) as exc_info:
        factorial('a')
    assert str(exc_info.value) == "Type Error: number must be positive integer"


if __name__ == "__main__":
    pytest.main([__file__])
