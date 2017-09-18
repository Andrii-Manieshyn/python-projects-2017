"""
Closest pair problem

The closest pair of points problem or closest pair problem is a problem of computational geometry:
given n points in metric space, find a pair of points with the smallest distance between them.
"""
from sys import maxsize
import math

def closest_pair_brute_force_algorithm(points):
    min_dist = maxsize
    for i in range(0, len(points)):
        for j in range(i + 1, len(points)):
            p, q = points[i], points[j]
            if dist(p, q) < min_dist:
                min_dist = dist(p, q)
                closest_pair = [p, q]
    return closest_pair

def dist(p, q):
    d = math.sqrt((q[0]-p[0]) ** 2 + (q[1]-p[1]) ** 2)
    return d
