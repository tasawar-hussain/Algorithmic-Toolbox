# Uses python3
import sys

def get_gcd(a, b):
    if b == 0:
        return a

    return get_gcd(b, a % b)

def lcm(a, b):
    gcd = get_gcd(a, b)
    product = a * b
    return product // gcd


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
