# Uses python3
import sys


def get_change(m):
    coins = [1, 3, 4]
    return solve(m, coins)


def solve(money, coins):
    min_num_coins = {0: 0}
    for m in range(1, money+1):
        min_num_coins[m] = float('inf')
        for coin in coins:
            if m >= coin:
                num_coins = min_num_coins[m-coin] + 1
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins
    return min_num_coins[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())

    print(get_change(m))
