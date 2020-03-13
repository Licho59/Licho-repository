#! python
# test_sample2.py - code for testing pytest library - great described by guru99 in post https://www.guru99.com/pytest-tutorial.html

import pytest

@pytest.mark.set1
def test_file2_method1():
    x, y = 5, 6
    assert x+1 == y, "test failed"
    assert x == y, "test failed because x=" + str(x) + " y=" + str(y)

@pytest.mark.set2    
def test_file2_method2():
    x, y = 5, 6
    assert x+1 == y, "test failed"
