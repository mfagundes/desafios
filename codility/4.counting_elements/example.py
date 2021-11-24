import time
import random

"""
Teste do enunciado do PDF da seção "Counting"

Avaliar o motivo pelo qual o resultado True sempre leva um tempo bem menor em Slow do que em Fast,
o que não está fazendo sentido - a menos que o swap ocorra com o primeiro valor de A
"""

def counting(A, m):
    """A é o array, m o valor máximo presente no array"""
    n = len(A)
    count = [0] * (m + 1)
    for k in range(n):
        count[A[k]] += 1
    return count


def slow_solution(A, B, m):  # Time complexity O(n**2)
    n = len(A)  # O(1)
    sum_a = sum(A)  # O(n)
    sum_b = sum(B)  # O(n)
    for i in range(n):  # O(n)
        for j in range(n):  # O(n)
            change = B[j] - A[i]  # O(1)
            sum_a += change  # O(1)
            sum_b -= change  # O(1)
            if sum_a == sum_b:
                return True
            sum_a -= change
            sum_b += change
    return False


def fast_solution(A, B, m):  # Time complexity O(n+m)
    n = len(A)
    sum_a = sum(A)  # O(n)
    sum_b = sum(B)  # O(n)
    d = sum_b - sum_a  # O(1)
    if d % 2 == 1:  # número ímpar (por que?)
        return False
    d //= 2
    count = counting(A, m)
    for i in range(n):
        if 0 <= B[i] - d and B[i] -d <= m and count [B[i] - d] > 0:
            return True
    return False


def test_solutions(A, B, m):
    start_slow_time = time.time()
    slow_res = slow_solution(A, B, m)
    slow_time = time.time() - start_slow_time

    start_fast_time = time.time()
    fast_res = fast_solution(A, B, m)
    fast_time = time.time() - start_fast_time

    return (slow_res, float(slow_time)), (fast_res, float(fast_time))


if __name__ == '__main__':
    num_tries = 10
    count_ = 1
    results = []

    while count_ <= num_tries:
        print(f"Tentativa {count_}")
        A = [random.randint(0,10) for _ in range(100)]
        B = [random.randint(0,10) for _ in range(100)]
        m = 10

        slow, fast = test_solutions(A, B, m)

        fast_over_slow = fast[1]/slow[1]
        results.append(fast_over_slow)

        print(f"Fast executou em {fast_over_slow:.6%} do tempo de Slow")

        print(f"Slow executou em {slow[1]: .10f} segundos - resultado: {slow[0]}")
        print(f"Fast executou em {fast[1]: .10f} segundos - resultado: {fast[0]}")

        print('==========================')
        count_ += 1

    for i, r in enumerate(results):
        if r > 1:
            print(f"Slow venceu na tentativa {i+1}")

    import statistics
    print(results)
    # print(f"Resultado final: na média, Fast executa em {statistics.mean(results): .4%}")