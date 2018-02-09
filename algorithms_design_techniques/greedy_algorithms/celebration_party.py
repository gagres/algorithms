import sys

def PointsCoverSorted(points):
    segments = []
    left = 0
    n = len(points)
    while left < n:
        value = int(points[left])
        l, r = value, value + 2
        segments.append((l, r))
        left = left + 1
        while left < n and int(points[left]) < r:
            left = left + 1
    return segments

points = list(input())
print(points)
print(PointsCoverSorted(points))