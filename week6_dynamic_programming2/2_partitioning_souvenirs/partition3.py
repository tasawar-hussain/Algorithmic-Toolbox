# Uses python3
import sys
import itertools


def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0


def partition_dp(souvenirs):
    total = sum(souvenirs)
    if total % 3 != 0:
        return 0

    size = total // 3
    n = len(souvenirs)

    count = 0
    table = [[0] * (n+1) for _ in range(size+1)]
    for i in range(1, size+1):
        for j in range(1, n+1):
            table[i][j] = table[i][j-1]
            if souvenirs[j-1] <= i:
                temp = table[i-souvenirs[j-1]][j-1] + souvenirs[j-1]
                if temp > table[i][j]:
                    table[i][j] = temp
            if table[i][j] == size:
                count += 1

    if count < 3:
        return 0
    else:
        return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition_dp(A))
