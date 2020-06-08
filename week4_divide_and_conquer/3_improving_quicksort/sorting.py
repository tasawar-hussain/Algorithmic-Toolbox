# Uses python3
import sys
import random

def partition3(a, l, r):
    pivot, left, right = a[l], l, r
    i = left
    while i <= right:
        if a[i] < pivot:
            a[left], a[i] = a[i], a[left]
            left += 1
        elif a[i] > pivot:
            a[right], a[i] = a[i], a[right]
            right -= 1
            i -= 1
        i += 1
    return (left, right)
    

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def get_pivot_index(arr, l, r):
    mid = l + (r-l)//2
    x = [(arr[l], l), ( arr[mid], mid), (arr[r], r)]
    x.sort()
    return x[1][1]

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1)
    randomized_quick_sort(a, m + 1, r)


def quick_sort(a, l, r):
    while l < r:
        k = get_pivot_index(a, l, r)
        a[l], a[k] = a[k], a[l]
        m1, m2 = partition3(a, l, r)
        if (m1-l) < (r-m2):
            quick_sort(a, l, m1 - 1)
            l = m2 + 1
        else:
            quick_sort(a, m2 + 1, r)
            r = m1 - 1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
