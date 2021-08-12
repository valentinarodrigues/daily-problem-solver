
class Solution:
    def get_balls(self, arr):
        def dfs(i, j, r, c):
            if(i == r):
                return j
            curr = arr[i][j]
            if(curr == 1 and (j+1 == c or arr[i][j+1] == -1)):
                return -1
            elif(curr == -1) and (j-1<0 or arr[i][j-1] == 1):
                return -1
            if(curr == 1):
                return dfs(i+1, j+1, r, c)
            else:
                return dfs(i+1, j-1, r, c)

        row , col = len(arr), len(arr[0])    
        ans = [-1] * col
        for idx in range(col):
            x = dfs(0, idx, row, col)
            ans[idx] = x
        return ans

s = Solution()
print(s.get_balls([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))