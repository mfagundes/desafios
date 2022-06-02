import numpy as np
from mutual_information import mutual_information

def test_1():
    x = [0.2, 0.3]
    y = [0.4, 0.5]
    arr = np.array([x, y])

    res = mutual_information(arr)
    for r in arr:
        print(r)
    assert res == 1