# Uses python3
import math


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def update_min_max(min_table, max_table, i, j, dataset):
    min_val, max_val = math.inf, -math.inf
    for k in range(i, j):
        oprtr = 2 * k + 1
        next_k = k + 1
        a = evalt(max_table[i][k], max_table[next_k][j], dataset[oprtr])
        b = evalt(max_table[i][k], min_table[next_k][j], dataset[oprtr])
        c = evalt(min_table[i][k], max_table[next_k][j], dataset[oprtr])
        d = evalt(min_table[i][k], min_table[next_k][j], dataset[oprtr])
        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)
    min_table[i][j], max_table[i][j] = min_val, max_val


def get_maximum_value(dataset):
    n = 1 + len(dataset) // 2
    min_table, max_table = [], []
    for i in range(n):
        min_table.append([0] * n)
        max_table.append([0] * n)
        min_table[i][i] = max_table[i][i] = int(dataset[2 * i])

    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            update_min_max(min_table, max_table, i, j, dataset)

    return max_table[0][-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
