# Uses python3
import sys


def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def optimal_sequence_dp(num):
    sequence = []
    dp = [0]*(num+1)
    # Fill table
    for i in range(1, len(dp)):
        dp[i] = dp[i-1] + 1
        if (i % 2 == 0):
            dp[i] = min(dp[i//2] + 1, dp[i])
        if (i % 3 == 0):
            dp[i] = min(dp[i//3] + 1, dp[i])
    while (num > 1):
        sequence.append(num)
        n = dp[num]-1
        if (dp[num-1] == n):
            num -= 1
        elif (num % 2 == 0 and (dp[num//2] == n)):
            num //= 2
        elif (num % 3 == 0 and (dp[num//3] == n)):
            num //= 3
    sequence.append(1)
    return reversed(sequence)


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence_dp(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
