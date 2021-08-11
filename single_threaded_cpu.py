from heapq import heappop,heappush
class Solution:
    def getOrder(self, tasks):
        tasks = sorted([(tasks[i][0], tasks[i][1], i) for i in range(len(tasks))])
        result, available = [], []
        cpu_time = tasks[0][0] # available for processing
        i = 0
        while i<len(tasks):
            # keep pushing available tasks as in tasks that have same or less start time (cpu_time)
            while i<len(tasks) and tasks[i][0] <= cpu_time:
                heappush(available, (tasks[i][1], tasks[i][2]))
                i+=1
            if available:
                (time, idx) = heappop(available) # min completion time will be poped
                cpu_time += time
                result.append(idx)
            elif i<len(tasks):
                cpu_time = tasks[i][0]
        while available:
            (d, idx) = heappop(available)
            result.append(idx)
        return result


s = Solution()
print(s.getOrder([[3,2],[1,2],[2,4],[4,1]]))