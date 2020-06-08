# python3
import sys


def compute_min_refills(distance, tank, stops):
    current_refill = 0
    num_refills = 0
    stops.insert(0, 0)
    if stops[-1] < distance:
        stops.append(distance)
    n = len(stops) - 2
    while current_refill <= n:
        last_refill = current_refill
        while current_refill <= n and (stops[current_refill + 1] - stops[last_refill] <= tank):
            current_refill += 1
        if last_refill == current_refill:
            return -1
        if current_refill <= n:
            num_refills += 1
    return num_refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))


# compute_min_refills(400,250,[100,150]) #output 1
# compute_min_refills(700, 200, [100, 200, 300, 400]) #-1
# compute_min_refills(1000, 200, [100, 200,250, 300, 400, 600, 780]) #-1
# compute_min_refills(1000, 200, [100, 200,250, 300, 400, 600, 780,820]) #5
# compute_min_refills(1000, 200, [100, 200,250, 300, 400, 600,820]) #-1
# compute_min_refills(1000, 200, [100, 200,250, 300, 400, 600,800]) #4
# compute_min_refills(10,3, [1,2,5,9]) #-1
# compute_min_refills(200,250,[100,150]) # 0
# compute_min_refills(1200, 400, [200, 375, 550, 750]) #-1
# compute_min_refills(1150, 400, [200, 375, 550, 750]) #2