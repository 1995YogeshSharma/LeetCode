'''
Given an integer array nums, return all the different possible non-decreasing subsequences of 
the given array with at least two elements. You may return the answer in any order.

'''

class Solution:
    '''
    backtracking solution. At each index, either we can consider current element or ignore it. 
    complexity 2^n
    '''
    result = set()
    input = []

    def is_nondecreasing(self, cur_list):
        if not cur_list or len(cur_list) == 1:
            return False

        cur = cur_list[0]
        for i in cur_list:
            if i < cur:
                return False
            cur = i
        return True

    def find_nondecreasing_subsequences(self, cur_list, idx):
        if idx >= len(self.input):
            if self.is_nondecreasing(cur_list):
                self.result.add(tuple(cur_list))
            return

        if idx < len(self.input):
            self.find_nondecreasing_subsequences(cur_list + [self.input[idx]], idx+1)
        self.find_nondecreasing_subsequences(cur_list, idx+1)

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.result = set()
        self.input = nums
        self.find_nondecreasing_subsequences([], 0)
        return [list(i) for i in list(self.result)]
        
