# Uses python3
def get_change(m):
    if m == 0:
        return 0
    ways = 0
    coins = [10, 5, 1]
    for coin in coins:
    	if m == 0:
    		break
    	if m >= coin:
    		count = m // coin
    		m = m % coin
    		ways = ways + count
    return ways

if __name__ == '__main__':
	m = int(input())
	print(get_change(m))
