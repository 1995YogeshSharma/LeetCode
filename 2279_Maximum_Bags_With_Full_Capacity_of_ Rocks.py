'''
You have n bags numbered from 0 to n - 1. You are given two 0-indexed integer arrays capacity and rocks. The ith bag can hold a maximum of capacity[i] rocks and currently contains rocks[i] rocks. You are also given an integer additionalRocks, the number of additional rocks you can place in any of the bags.

Return the maximum number of bags that could have full capacity after placing the additional rocks in some bags.
'''

import heapq

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        '''
        We can find remaining capacity and put it in max heap, then pick from min heap 
        one by one, to consume additionalRocks.
        '''
        remaining_capacity = [capacity[i] - rocks[i] for i in range(0, len(rocks))]
        heapq.heapify(remaining_capacity)

        count = 0
        while len(remaining_capacity) > 0:
            current = heapq.heappop(remaining_capacity)

            additionalRocks -= current

            if additionalRocks >= 0:
                count += 1

        return count
