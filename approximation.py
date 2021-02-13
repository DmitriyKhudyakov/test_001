import numpy as np


KI_LIST = [[1, 0], [2, 1], [4, 2], [7, 3]]


def psi(num_p, k, exp_data):
    global KI_LIST
    i = 0
    for ki_curr in KI_LIST:
        if k >= ki_curr[0]:
            i = ki_curr[1]
        else:
            break
    j = k - 1 - i * (1 + i) / 2.0
    power = [i - j, j]
    return (exp_data[num_p][0] ** power[0]) * (exp_data[num_p][1] ** power[1])


def calc_a(exp_data, n):
    a = [[0.0] * n for i in range(n)]
    for n1 in range(1, n + 1):
        for n2 in range(1, n + 1):
            a_curr = 0.0
            for n3 in range(len(exp_data)):
                a_curr += psi(n3, n2, exp_data) * psi(n3, n1, exp_data)
            a[n1 - 1][n2 - 1] = a_curr
    return a


def calc_b(exp_data, n):
    b = []
    for n1 in range(1, n + 1):
        b_curr = 0.0
        for n2 in range(len(exp_data)):
            b_curr += exp_data[n2][2] * psi(n2, n1, exp_data)
        b.append(b_curr)
    return b


def calc(exp_data, n):
    a = calc_a(exp_data, n)
    b = calc_b(exp_data, n)
    return np.linalg.solve(np.array(a), np.array(b))
