#! python
# test_sample1.py - code for testing pytest library - great described by guru99 in post https://www.guru99.com/pytest-tutorial.html

import pytest
# py.test - executable command for all files in directory; 
# with options -k <arg>(run by substring matching) and -m <arg> (run by markers with decorators over function definition) 

@pytest.mark.set1
def test_file1_method1():
    x  = 5
    y = 6
    assert x + 1 == y, "test failed"
    assert x == y, "test failed because x=" + str(x) + " y=" + str(y)

@pytest.mark.set1    
def test_file1_method2():
    x = 5
    y = 6
    assert x+1 == y, "test failed"
