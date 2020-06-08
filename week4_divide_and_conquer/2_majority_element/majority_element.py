# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    return -1


def get_majority(arr, left, right):
    if right - left == 1:
        return arr[left]
    mid = left + (right - left) // 2
    ml = get_majority(arr, left, mid)
    mr = get_majority(arr, mid, right)
    temp = arr[left:right]
    n = len(temp)
    count = temp.count(ml)
    if count > n//2:
        return ml
    count = temp.count(mr)
    if count > n//2:
        return mr
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority(a, 0, n) != -1:
        print(1)
    else:
        print(0)
