class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(len(manager)):
            graph[manager[i]].append(i)
        
        def dfs(u):
            ans = 0
            for v in graph[u]:
                ans = max(dfs(v) + informTime[u], ans)
            return ans
        
        return dfs(headID)


Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]