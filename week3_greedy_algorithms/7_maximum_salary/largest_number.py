#Uses python3

import sys
from functools import cmp_to_key

def is_better(a,b):
    return int(b+a) - int(a+b)

def largest_number(a):
    arr = sorted(a, key=cmp_to_key(is_better))
    return int(''.join(map(str, arr)))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))