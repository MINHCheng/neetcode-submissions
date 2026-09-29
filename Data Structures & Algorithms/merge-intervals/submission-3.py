class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda i : i[0])
        newInterval = intervals[0]
        for i in range(len(intervals)):

            if intervals[i][1] < newInterval[0]:
                print(intervals[i])
                newInterval = intervals[i]
                res.append(intervals[i][1])
            elif intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                newInterval = intervals[i]
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        res.append(newInterval)
        return res

        