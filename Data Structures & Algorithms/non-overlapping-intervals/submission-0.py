class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])
        count = 0
        newInterval = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][1] <= newInterval[0]:
                continue
            if intervals[i][0] >= newInterval[1]:
                newInterval = intervals[i]
            else:
                newInterval = [max(newInterval[0], intervals[i][0]), 
                min(newInterval[1], intervals[i][1])]
                print(newInterval)
                count +=1
        return count