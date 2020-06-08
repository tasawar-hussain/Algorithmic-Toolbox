# Uses python3
import sys


def optimal_weight(capacity, bars):
    m, n = len(bars) + 1, capacity + 1
    mem = [[0] * n for _ in range(m)]
    for i in range(1, m):
        wt = bars[i - 1]
        for capacity in range(1, n):
            mem[i][capacity] = mem[i - 1][capacity]
            if wt <= capacity:
                value = mem[i - 1][capacity - wt] + wt
                if mem[i][capacity] < value:
                    mem[i][capacity] = value

    return mem[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
