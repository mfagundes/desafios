from cyclic_rotation import solution
"""
Test 1
    A = [3, 8, 9, 7, 6]
    K = 3
returns
    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
    
Test 2:
    A = [0, 0, 0]
    K = 1
returns
    [0, 0, 0]
    
Test 3
    A = [1, 2, 3, 4]
    K = 4
returns
    [1, 2, 3, 4]
    
Assumptions
- N and K are integers within the range [0..100];
- each element of array A is an integer within the range [−1,000..1,000].
"""

def test_empth():
    assert solution([]) == []

def test_1():
    assert solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]

def test_2():
    assert solution([0, 0, 0], 1) == [0, 0, 0]

def test_3():
    assert solution([1, 2, 3, 4], 4) == [1,2,3,4]