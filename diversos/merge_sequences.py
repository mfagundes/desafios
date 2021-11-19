# Dadas as sequencias ordenadas e descontínuas...

a = [1, 2, 3, 4]
b = [1, 3, 4, 5, 6, 7]
c = [3, 6, 8, 9, 10]

# Sabendo que o resultado esperado é...

expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Como você gera uma sequência:
# 1. de elementos únicos
# 2, respeitando a ordem
# 3. com espaço de memória constante
# 4. e tempo de execução linear

## Sorted e set: não implementa as restrições 3 e 4
print(sorted(set((*a, *b, *c))))

## Usando o heapq.merge para percorrer cada lista uma vez
# Não respeita elementos únicos
from heapq import merge
print(list(merge(a, b, c)))

# Usando o merge para garantir elementos únicos
def unique(*it):
    values, previous = merge(*it), merge(*it)
    yield next(values)
    yield from (v for v, p in zip(values, previous) if p!= v)

print(list(unique(a, b, c)))

