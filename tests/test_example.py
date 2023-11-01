import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from src.example import add, subtract # noqa: E402


def test_add():
    assert add(1, 2) == 3


def test_subtract():
    assert subtract(5, 2) == 3
