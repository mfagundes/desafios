from perm_missing_element import solution

def test_2():
    assert solution([1,2,3,4,5,6,7,8,10,11,12,13,14]) == 9

def test_1():
    assert solution([2,3,1,5]) == 4
