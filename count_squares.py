# Best explanation https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/643429/Python-DP-Solution-%2B-Thinking-Process-Diagrams-(O(mn)-runtime-O(1)-space)
class Solution:
    def countSquares(self, matrix) -> int:
        row = len(matrix)
        col = len(matrix[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if(matrix[i][j] == 1):
                    if(i>0 and j>0):
                        matrix[i][j] += min(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j])
                    count+=matrix[i][j]
                        
        return count
                    
                    
s = Solution()
print(s.countSquares([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]))