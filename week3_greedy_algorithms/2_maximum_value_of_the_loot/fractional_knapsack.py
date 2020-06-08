# Uses python3
import sys

from operator import itemgetter

def get_optimal_value(capacity, weights, values):
    size = len(weights)
    ratios = [None] * size
    value = 0
    for i in range(size):
        ratios[i] = (values[i] / weights[i], i)
    ratios.sort(key=itemgetter(0), reverse=True)
    for item in ratios:
        if capacity == 0:
            break
        (ratio, index) = item
        amount = min(weights[index], capacity)
        value = value + amount * ratio
        weights[index] = weights[index] - amount
        capacity = capacity - amount
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))