from math import *
from tracemalloc import start
from collections import deque
from functools import cmp_to_key


def adjust(angle):
    if angle < 0:
        angle += 360
    return angle


def find_angles(circle):
    cx = circle[0]
    cy = circle[1]
    r = circle[2]

    dx, dy = px - cx, py - cy
    dxr, dyr = -dy, dx
    d = (dx ** 2 + dy ** 2) ** 0.5

    rho = r / d
    ad = rho ** 2
    bd = (rho ** 2 * (1 - rho ** 2)) ** 0.5
    t1x = cx + ad * dx + bd * dxr
    t1y = cy + ad * dy + bd * dyr
    t2x = cx + ad * dx - bd * dxr
    t2y = cy + ad * dy - bd * dyr

    t1 = atan2(t1y - py, t1x - px) * 180 / pi
    t2 = atan2(t2y - py, t2x - px) * 180 / pi

    return [t1, t2]


def sort_and_reduce(intervals):
    intervals.sort(key=lambda x: x[1])
    intervals.sort(key=lambda x: x[0])
    result = []
    for cur_interval in intervals:
        while result and result[-1][1] >= cur_interval[1]:
            result.pop()
        result.append(cur_interval)
    return result


def max_non_overlapping(perimeter, intervals):
    intervals = sort_and_reduce(intervals)
    ans = 0
    schedules = deque()
    more_schedules = True
    for cur_interval in intervals:
        if more_schedules:
            if not schedules or cur_interval[0] <= intervals[0][1]:
                schedules.append([cur_interval])
                continue
            else:
                more_schedules = False
        if cur_interval[0] > schedules[0][-1][1]:
            if cur_interval[1] < perimeter:
                while len(schedules) > 1 and cur_interval[0] > schedules[1][-1][1]:
                    schedules.popleft()
                schedules[0].append(cur_interval)
                schedules.append(schedules.popleft())
            else:
                while schedules and cur_interval[0] > schedules[0][-1][1] and \
                        cur_interval[1] < perimeter + schedules[0][0][0]:
                    ans = max(ans, 1 + len(schedules.popleft()))
                while schedules and cur_interval[1] >= perimeter + schedules[0][0][0]:
                    ans = max(ans, len(schedules.popleft()))
                while schedules and cur_interval[0] > schedules[0][-1][1] and \
                        cur_interval[1] < perimeter + schedules[0][0][0]:
                    ans = max(ans, 1 + len(schedules.popleft()))
                if not schedules:
                    break
    print(schedules)
    for q in schedules:
        for item in q:
            print(item[1], ',', end='')
    print()
    return max(ans, len(schedules[-1]) if schedules else 0)


fin = open('input.txt', 'r')
px, py = map(float, fin.readline().split())
circles = []

point = []

for line in fin:
    circles.append(list(map(float, line.split())))

angles = [find_angles(b) for b in circles]
perimeter = 360.0
for i in range(len(angles)):
    for j in range(2):
        angles[i][j] = adjust(angles[i][j])
        if angles[i][0] > angles[i][1]:
            angles[i][1] += 360

intervals = angles
res = max_non_overlapping(perimeter, intervals)
print(res)

fin.close() 
