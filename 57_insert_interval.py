'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
represent the start and the end of the ith interval and intervals is sorted in ascending order by 
starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by 
starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        - Go over interval and insert the newInterval wherever fits
        - Create auxiliary array and merge intervals in the 'intervals' list
        '''
        # insert
        is_inserted = False
        for i in range(0, len(intervals)):
            if i == 0:
                if newInterval[0] < intervals[i][0]:
                    intervals = [newInterval] + intervals
                    is_inserted = True
                    break

            else:
                if newInterval[0] < intervals[i][0]:
                    intervals = intervals[0:i] + [newInterval] + intervals[i:]
                    is_inserted = True
                    break

        if not is_inserted:
            intervals = intervals + [newInterval]

        # print (intervals)

        # merge intervals
        result = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if end < intervals[i][0]:
                result.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            
            else:
                end = max(intervals[i][1], end)

        result.append([start, end])

        return result
