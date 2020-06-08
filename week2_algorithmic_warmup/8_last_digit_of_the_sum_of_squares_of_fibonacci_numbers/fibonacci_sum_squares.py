# Uses python3
def get_pisano_period_length(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
        if (previous == 0 and current == 1):
            return i + 1

def get_fibonacci(n):
    if (n <= 1):
        return n
    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current

def get_fibonacci_huge(n, m):
    if n <= 1:
        return n
    pisano_period_length = get_pisano_period_length(m)
    periodic_fib = get_fibonacci(n % pisano_period_length)
    return periodic_fib % m

def fibonacci_sum_squares(n):
    if n <= 1:
        return n
    sum = get_fibonacci_huge(n, 10) * get_fibonacci_huge(n+1, 10)
    return sum % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
