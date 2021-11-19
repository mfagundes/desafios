from arrays_oddoccurenciesinarray import solution, solution_mf
from datetime import datetime

REPETITIONS = 1000000

def test_mf():
    # 1,1,2,2,3,4,4,5,5,6,6
    res = []
    begin = datetime.now()
    for i in range(REPETITIONS):
        res.append(solution_mf([1,4,6,2,1,3,5,5,6,4,2]))
    print(datetime.now() - begin)
    assert len(res) == REPETITIONS
    assert res[9] == 3
    # assert solution([1,4,6,2,1,3,5,5,6,4,2]) == 3

def test_6():
    # 1,1,2,2,3,4,4,5,5,6,6
    res = []
    begin = datetime.now()
    for i in range(REPETITIONS):
        res.append(solution([1,4,6,2,1,3,5,5,6,4,2]))
    print(datetime.now() - begin)
    assert len(res) == REPETITIONS
    assert res[9] == 3
    # assert solution([1,4,6,2,1,3,5,5,6,4,2]) == 3

def test_5():
    # 1,1,2,2,3
    assert solution([1,2,3,1,2]) == 3

def test_4():
    assert solution([1,1,2]) == 2

def test_3():
    assert solution([1]) == 1


def test_2():
    assert solution([5,1,2,3,4,1,2,3,4]) == 5


def test_1():
    assert solution([9,3,9,3,9,7,9]) == 7
