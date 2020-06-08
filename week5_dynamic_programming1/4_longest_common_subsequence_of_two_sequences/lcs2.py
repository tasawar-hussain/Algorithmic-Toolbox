# Uses python3

import sys


def lcs_memoized(p, q, n, m, dp):
    if dp[n][m] is not -1:
        return dp[n][m]
    if n == 0 or m == 0:
        result = 0
    elif p[n-1] == q[m-1]:
        result = 1 + lcs_memoized(p, q, n-1, m-1, dp)
    else:
        tmp1 = lcs_memoized(p, q, n-1, m, dp)
        tmp2 = lcs_memoized(p, q, n, m-1, dp)
        result = max(tmp1, tmp2)
    dp[n][m] = result
    return result


def lcs2(a, b):
    n = len(a)
    m = len(b)
    mem = [[-1 for x in range(m+1)] for y in range(n+1)]
    for i in range(n+1):
        mem[i][0] = 0
    for i in range(m+1):
        mem[0][i] = 0
    return lcs_dp(a, b, mem)


def lcs_dp(a, b, mem):
    x = [None] + a
    y = [None] + b
    for i in range(1, len(x)):
        for j in range(1, len(y)):
            if x[i] == y[j]:
                mem[i][j] = 1 + mem[i-1][j-1]
            else:
                mem[i][j] = max(mem[i-1][j], mem[i][j-1])
    return mem[len(a)][len(b)]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
