'''
You are given a positive integer array nums.

The element sum is the sum of all the elements in nums.
The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
Return the absolute difference between the element sum and digit sum of nums.

Note that the absolute difference between two integers x and y is defined as |x - y|.
'''

class Solution:
    def digit_sum(self, num):
        digit_sum = 0
        while num > 0:
            digit_sum += num%10
            num = num//10
            
        return digit_sum
            
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = 0
        digital_sum = 0
        
        for i in nums:
            element_sum += i
            digital_sum += self.digit_sum(i)
            
        return element_sum - digital_sum
        
