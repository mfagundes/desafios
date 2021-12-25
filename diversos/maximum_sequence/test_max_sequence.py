import pytest

"""
Crie um programa para encontrar a sub-sequência contínua dentro do array A que possua maior soma:

Exemplo 1:
Input: [-1, 5, 2, 1, 4, -7, 8, -3, -4, 2]
Output: 13

Neste primeiro exemplo, o subarray [5, 2, 1, 4, -7, 8] é a sequência contínua de maior 
soma contida dentro do array e a soma deste array é 13

Exemplo 2:
Input: [6, -4, -2, 1, -3, 5, -1, 2, 1, 1, -5, 4]
Output: 8

Neste segundo exemplo, o subarray [5, -1, 2, 1, 1] é a sequência contínua de maior soma 
contida dentro do array e a soma destes número é 8.

Seu programa só precisa exibir o VALOR da maior soma, não é necessário exibir o array em questão.

"""
from diversos.maximum_sequence.max_sequence import max_sequence


def test_1():
    numbers = [-1, 5, 2, 1, 4, -7, 8, -3, -4, 2]
    assert max_sequence(numbers) == 13


def test_2():
    numbers = [6, -4, -2, 1, -3, 5, -1, 2, 1, 1, -5, 4]
    assert max_sequence(numbers) == 8


def test_3():
    numbers = [1, 2, 3, 4]
    assert max_sequence(numbers) == 10


def test_4():
    numbers = [1, 2, -1, 4]
    assert max_sequence(numbers) == 6


def test_5():
    numbers = [-1, 5, 2, 1, 4, -11, 14, -3, -4, 2]
    assert max_sequence(numbers) == 15


def test_6():
    numbers = [-1, -4, -3]
    assert max_sequence(numbers) == -1


def test_7():
    numbers = [5, -1, -3]
    assert max_sequence(numbers) == 5


def test_8():
    numbers = [-4, -3, -2]
    assert max_sequence(numbers) == -2


def test_9():
    numbers = [6, -1, -3, 5]
    assert max_sequence(numbers) == 7


def test_invalid_sequence():
    numbers = [-1, 5, 2, 1, 'quatro', -11, 14, -3, -4, 2]
    with pytest.raises(ValueError) as e:
        max_sequence(numbers)
    assert "Lista deve ser de inteiros" in str(e.value)


def test_invalid_sequence_2():
    numbers = [-1, 5, 2, 1, 4.0, -11, 14, -3, -4, 2]
    with pytest.raises(ValueError) as e:
        max_sequence(numbers)
    assert "Lista deve ser de inteiros" in str(e.value)
