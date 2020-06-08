# Uses python3
import sys


def merge_n_count(actual, temp, left, right, mid):
    i, j, k = left, mid + 1, left
    inv_count = 0
    while i <= mid and j <= right:
        if actual[i] <= actual[j]:
            temp[k] = actual[i]
            i += 1
        else:
            temp[k] = actual[j]
            inv_count += (mid-i + 1)
            j += 1
        k += 1
    while i <= mid:
        temp[k] = actual[i]
        k += 1
        i += 1
    while j <= right:
        temp[k] = actual[j]
        k += 1
        j += 1
    for idx in range(left, right + 1):
        actual[idx] = temp[idx]
    return inv_count

def number_of_inversions(a, b, left, right):
    inversions_count = 0
    if right - left < 1:
        return inversions_count
    mid = (right + left) // 2
    inversions_count += number_of_inversions(a, b, left, mid)
    inversions_count += number_of_inversions(a, b, mid+1, right)
    inversions_count += merge_n_count(a, b, left, right, mid)
    return inversions_count


def solve(arr):
    n = len(arr)
    b = n * [0]
    return number_of_inversions(arr, b, 0, n-1)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))

    print(solve(a))







