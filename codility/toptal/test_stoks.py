from stocks import solution
def test_1():
    files =["./data/framp.csv"]
    assert solution(files) is False