# Uses python3

import sys


def lcs3(a, b, c):
    m = len(a)
    n = len(b)
    p = len(c)
    dp = [[[0 for k in range(p+1)] for j in range(n+1)]
          for i in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            for k in range(1, p+1):
                if(a[i-1] == b[j-1] == c[k-1]):
                    dp[i][j][k] = 1 + dp[i-1][j-1][k-1]
                else:
                    val = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
                    dp[i][j][k] = val
    return dp[-1][-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
