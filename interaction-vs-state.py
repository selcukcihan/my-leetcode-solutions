from typing import List
import unittest
from unittest.mock import MagicMock


class Number:
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return f"{self._value}"

    def compare_to(self, that):
        return self._value - that._value

    def value(self):
        return self._value


def find_max_(numbers: List[Number]):
    max = None
    for n in numbers:
        if max is None or max.compare_to(n) < 0:
            max = n
    return max


def find_max(numbers: List[Number]):
    max = None
    for n in numbers:
        if max is None or max.value() < n.value():
            max = n
    return max


class Test(unittest.TestCase):
    def test(self):
        # given
        n1 = Number(10)
        n2 = Number(20)

        # when
        result = find_max([n1, n2])

        # then
        self.assertTrue(result is n2, f"max value is {result.value()}")

    def test_v1(self):
        # given
        n1 = MagicMock()
        n1.value.return_value = 10
        n2 = MagicMock()
        n2.value.return_value = 20

        # when
        result = find_max([n1, n2])

        # then
        self.assertTrue(result is n2, f"max value is {result.value()}")


if __name__ == "__main__":
    unittest.main()


# print(find_max_v1([Number(10), Number(20), Number(-10)]))
# print(find_max_v2([Number(10), Number(20), Number(-10)]))
