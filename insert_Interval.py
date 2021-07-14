class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        n = len(intervals)
        start, end = newInterval
        idx = 0
        while(idx < n and start>intervals[idx][0]):
            result.append(intervals[idx])
            idx+=1
        
        # if result is empty 
        if not result or result[-1][1] < start:
            result.append(newInterval)
        else:
            result[-1][1] = max(end, result[-1][1])
        
        while(idx<n):
            interval = intervals[idx]
            start, end = interval
            idx+=1
            
            if result[-1][1] < start:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], end)
        return result

# [[1, 3], [5, 9]] 
#  [2, 5]


