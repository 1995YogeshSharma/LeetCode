'''
A binary string is monotone increasing if it consists of some number of 0's (possibly none), 
followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.
'''

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        '''
        consider how to make string of size 'n' monotonic

        if we know that uptill size 'n-1', it is monotonic -> 
        if '1' -> no need for flip take count('n-1')
        if '0' -> either flip all 1s encountered before this or flip the '0' itself.
        '''
        ans = 0
        count_1_in_prefix = 0
        for c in s:
            if c == '0':
                ans = min(count_1_in_prefix, ans + 1)
            else:
                count_1_in_prefix += 1
        return ans

      
