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

    # sendo os arrays inteiros, a solução, conforme explicada abaixo, sempre será False
    # se a diferença entre as somas for ímpar
    if d % 2 == 1:
        return False

    # a diferença entre as somas é dividida por 2 e este será o valor que, no swap, será
    # adicionado à menor soma e subtraído da maior. Assim, para cada valor de B é necessário
    # checar se no array A existe um inteiro que seja igual ao valor de B menos a metade da
    # diferença das somas. Isso confirma que, naquele ponto de B, existe em A um valor que
    # é igual a esse valor de B menos a diferença. Por exemplo:
    #
    # a = [1,2,3] (soma = 6)
    # b = [4,5,7] (soma = 16)
    3
    # A diferença entre os arrays é de 10, assim é preciso tirar 5 de um array e somar ao outro
    # Isso ocorrerá se o valor de B menos a metade da diferença existir em A. No exemplo temos em
    # B[2] o valor 7, que subtraído da metade da diferença dará 2. Precisamos, então, que o valor
    # 2 exista no array A. Isso se verifica observando se count[2] > 0
    d //= 2
    count = counting(A, m)
    for i in range(n):
        # se o valor B[i] subtraído da metade da diferença estiver fora dos conjunto de inteiros
        # possíveis no problema (0 <= N <= m) não existirá um valor possível em A
        if 0 <= B[i] - d and B[i] -d <= m and count[B[i] - d] > 0:
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