# Uses python3
import sys
from itertools import chain

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    start_labelled = zip(starts, [float('-inf')]*len(starts))
    end_labelled = zip(ends, [float('inf')]*len(ends))
    points_lablled = zip(points, range(len(points)))
    concated_list = chain(start_labelled, end_labelled, points_lablled)
    sorted_list = sorted(concated_list, key=lambda a : (a[0], a[1]))
    stack = []
    for x, y in sorted_list:
        if y == float('-inf'):
            stack.append(y)
        elif y == float('inf'):
            stack.pop()
        else:
            cnt[y] = len(stack)
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')


