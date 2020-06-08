# Uses python3
import sys


def nth_consective_sum(n):
    start = 2
    while True:
        res = (start*(start+1))//2
        if res >= n:
            break
        start +=1
    return (start, res)


def optimal_summands(n):
    if n<3:
        return [n]
    summands = []
    num , total = nth_consective_sum(n)
    if total == n:
        summands = list(range(1, num+1))
    else:
        sum_ = num*(num-1)//2
        summands = list(range(1, num))
        summands[-1] = summands[-1] + (n-sum_)
    return summands

    
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
