'''
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of 
nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], 
nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
'''

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        '''
        Either array can be simple max subarray sum (kadane solution)
        Otherwise, we can consider the solution to contain sum part from start, 
            some part from end.
        

        '''
        cur_max = 0
        max_sum = nums[0]

        cur_min = 0
        min_sum = nums[0]

        sum = 0

        # iterate over array to find max_sum and min_sum, 
        # if sum of whole array is min_sum,  
        for num in nums:
            cur_max = max(cur_max, 0) + num
            max_sum = max(max_sum, cur_max)

            cur_min = min(cur_min, 0) + num
            min_sum = min(min_sum, cur_min)
            sum += num
        
        return max_sum if sum == min_sum else max(max_sum, sum - min_sum);
    
