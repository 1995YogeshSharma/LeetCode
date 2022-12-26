'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

'''

'''
Solution - 
top down DP O(n^2)
Iterate right to left, keep leftMostJumpable O(n)
'''

from typing import List

class Solution:
    visitable: List[int] = []
    leftMostJumpable: int = -1

    def checkJump(self, nums: List[int], idx: int):
        if idx + nums[idx] >= self.leftMostJumpable:
            self.leftMostJumpable = idx
            return

    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        self.visitable = [-1]*length

        self.visitable[length - 1] = 1

        self.leftMostJumpable = length - 1
        for i in range(length-2, -1, -1):
            self.checkJump(nums, i)

        return self.leftMostJumpable == 0


