# test_main.py

from main import add

def test_add():
    assert add(2, 3) == 5

def test_add_negative_positive():
    assert add(-1, 1) == 0
