# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def get_common(index, points):
    common = points[index]
    while True and index + 1 < len(points):
        next_ = points[index + 1]
        if common[1] < next_[0]:
            break
        common = (max(common[0], next_[0]), min(common[1], next_[1]))
        index += 1
    return (index, common[1])

def optimal_points(segments):
    segment_tuples  = []
    for s in segments:
        segment_tuples.append((s.start, s.end))
    segment_tuples.sort()
    result = []
    start = 0
    while start < len(segments):
        start, common = get_common(start, segment_tuples)
        result.append(common)
        start += 1
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)