import math


def euclidean_distance_2d(point1, point2):
    x1, x2 = point1[0], point2[0]
    y1, y2 = point1[1], point2[1]
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance
