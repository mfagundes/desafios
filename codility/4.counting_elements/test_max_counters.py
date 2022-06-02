from max_counters import solution


def test_1():
    N = 1
    A = [1, 2]
    counters = solution(N, A)
    assert counters == [1]

def test_2():
    N = 1
    A = [1, 2]
    counters = solution(N, A)
    assert counters == [1]

def test_3():
    N = 2
    A = [3, 1, 6]
    counters = solution(N, A)
    assert counters == [1, 0]

def test_4():
    N = 1
    A = [3]
    counters = solution(N, A)
    assert counters == [0]


def test_100():
    N = 5
    A = [3, 4, 4, 6, 1, 4, 4]
    counters = solution(N, A)
    assert counters == [3,2,2,4,2]