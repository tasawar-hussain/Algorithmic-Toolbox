# Uses python3
def edit_distance(s, t):
    n = len(s) + 1
    m = len(t) + 1
    dp = [[0 for x in range(m)] for y in range(n)]
    for i in range(n):
        dp[i][0] = i
    for i in range(m):
        dp[0][i] = i
    dist = 0
    for i in range(1, n):
        for j in range(1, m):
            dist = 1
            if(s[i-1] == t[j-1]):
                dist = 0
            d = min(dp[i-1][j], dp[i][j-1])
            dp[i][j] = min(d + 1, dp[i-1][j-1] + dist)
    return dp[n-1][m-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
