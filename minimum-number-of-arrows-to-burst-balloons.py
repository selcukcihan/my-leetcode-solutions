from typing import List


# There are some spherical balloons taped onto a flat wall
# that represents the XY-plane.
# The balloons are represented as a 2D integer array points
# where points[i] = [xstart, xend] denotes a balloon
# whose horizontal diameter stretches between xstart and xend.
# You do not know the exact y-coordinates of the balloons.
# Arrows can be shot up directly vertically (in the positive y-direction)
# from different points along the x-axis.
# A balloon with xstart and xend is burst by an arrow
# shot at x if xstart <= x <= xend.
# There is no limit to the number of arrows that can be shot.
# A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.


# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 1-6, 2-8, 7-12, 10-16
        points = sorted(points, key=lambda x: x[0])
        current_range = None
        shots = 0
        for point in points:
            begin = point[0]
            end = point[1]
            if current_range is None:
                current_range = [begin, end]
            else:
                if begin > current_range[1] or end < current_range[0]:
                    shots += 1
                    current_range = [begin, end]
                    continue

                if begin > current_range[0]:
                    current_range[0] = begin
                if end < current_range[1]:
                    current_range[1] = end
        if current_range is not None:
            shots += 1
        return shots
