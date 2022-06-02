import numpy as np

def mutual_information(arr):
    # marginal distribution j
    p_i = []
    p_j = []
    for row in arr:
        p_i.append(sum([p * np.log(p) for p in row]))
    print(p_i)
    for col in arr.transpose():
        p_j.append(sum([p * np.log(p) for p in col]))
    print(p_j)

    p_ij = 0
    for p in np.nditer(arr):
        p_ij += p * np.log(p)
    print(p_ij)
    return p_ij - sum(p_i) - sum(p_j)