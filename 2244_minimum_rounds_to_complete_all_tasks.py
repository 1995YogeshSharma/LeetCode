'''
You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the same difficulty level.

Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.
'''

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        '''
        Consider 'k' groups, then frequency of each number can be represented as
        f[t[i]] = 3k (f[t[i]] / 3 groups needed)
        f[t[i]] = 3k + 1 (if k == 0, not possible, else can be represented as 3(k-1) + 2*2, f[t[i]] / 3 + 1 group needed)
        f[t[i]] = 3k + 2 (f[t[i]]/3 + 1 group needed)
        '''

        freq = {}
        for i in tasks:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1
        
        min_rounds = 0
        for key, value in freq.items():
            if value == 1:
                return -1
            
            elif value % 3 == 0:
                min_rounds += value // 3
            
            else:
                min_rounds += value // 3 + 1

        return min_rounds

