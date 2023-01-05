'''
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.


'''

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
        Sort array on start time.
        For current index, we can cover all the balloons that end before the current end time. 
        We need to take a running count of number of arrows needed. If we encounter some range where end point is less than current end point,
        we need to update the end point to that.
        '''
        points_sorted = sorted(points, key=lambda k: k[0])

        count = 1
        leftmost_end = points_sorted[0][1]

        for value in points_sorted:
            if value[0] > leftmost_end:
                count += 1
                leftmost_end = max(leftmost_end, value[1])
            leftmost_end = min(leftmost_end, value[1])

        return count
