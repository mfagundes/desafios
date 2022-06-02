import pytest


def two_sum(nums, target):
    for i, a in enumerate(nums):
        for j, b in enumerate(nums):
            if i == j:
                continue

            if a + b == target:
                return [i, j]

    for i, a in enumerate(nums[:-1]):
        for j, b in enumerate(nums[1:], start=1):
            if a + b == target:
                return [i, j]

    for i in range(0, len(nums) - 1):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum(nums, target):
    seen = {nums[0]: 0}

    for i, n in enumerate(nums[1:], start=1):
        v = target - n
        if v in seen:
            return [seen[v], i]
        else:
            seen[n] = i


"""
def test_exemplo3():
    assert two_sum([3, 3], 6) == [0, 1]
"""


def test_exemplo2():
    assert two_sum([3, 2, 4], 6) == [1, 2]


"""

def test_exemplo2b():
    assert two_sum([3, 2, 4], 5) == [0, 1]

def test_exemplo2c():
    assert two_sum([3, 2, 4], 7) == [0, 2]

def test_exemplo1():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_exemplo1b():
    assert two_sum([2, 7, 11, 15], 26) == [2, 3]
"""
if __name__ == "__main__":
    pytest.main(["-s", __file__])

"""
Lista
1. Augusto
2. Diogo Bueno
3. Getulio Castro (plateia)
4. Túlio Chiodi (plateia)
5. Anderson Alves(plateia) OFF
6. Hand Medeiros
7. Cássio Augusto
8. André Delorme
9. Mauricio Fagundes
10. Fernando Rodrigues
"""