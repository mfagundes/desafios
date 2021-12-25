def max_sequence(numbers: list) -> int:
    cumsums = []
    acc = 0
    for number in numbers:
        if not isinstance(number, int):
            raise ValueError("Lista deve ser de inteiros")
        acc += number
        cumsums.append(acc)
    min_sum = min(cumsums)
    if min_sum < 0:
        cumsum_adjusted = [i - min_sum for i in cumsums]
    else:
        cumsum_adjusted = cumsums
    return max(numbers) if all(n < 0 for n in numbers) else max(cumsum_adjusted)