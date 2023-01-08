'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, 
return the maximum number of points that lie on the same straight line.
'''

import math
class Solution:

    def maxPoints(self, points: List[List[int]]) -> int:
        '''
        consider each point as starting point and get slopes for other points from this point
        return the maximum number of slopes found.
        '''

        max_lines = 0
        for i in range(0, len(points)):
            slopes = {}
            for j in range(i+1, len(points)):
                slope = self.calculate_slope(points[i], points[j])

                if slope not in slopes:
                    slopes[slope] = 0

                slopes[slope] += 1

                max_lines = max(max_lines, slopes[slope])

        return max_lines + 1

    def calculate_slope(self, a: List, b: List):
        x1,y1 = a[0], a[1]
        x2,y2 = b[0], b[1]

        if x2 == x1:
            return math.inf

        return (y2 - y1) / (x2 - x1)

        
