# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    if (n == 2):
        return 1

    a = 1
    b = 1
    result = 0

    for i in range(2,n):
        result = a + b
        a = b
        b = result

    return result


# fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811]
#
# for idx, val in enumerate(fibs):
#     res = calc_fib(idx)
#     if  res == val:
#         print("True")
#     else:
#         print(res, idx, val )

n = int(input())
print(calc_fib(n))
