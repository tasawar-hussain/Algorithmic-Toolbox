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

if __name__ == '__main__':
    data  = input();
    n, m = map(int, data.split())
    print(get_fibonacci_huge(n, m))







def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
        if (previous == 0 and current == 1):
            return i + 1


def fibonacciModulo(n, m):
    # Getting the period
    pisano_period = pisanoPeriod(m)
    n = n % pisano_period
    previous, current = 0, 1
    if n <= 1:
        return n
    for i in range(n-1):
        previous, current = current, previous + current
    return (current % m)
