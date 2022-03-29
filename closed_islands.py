
# class Solution:
#     def closedIsland(self, grid) -> int:
#         rows = len(grid)
#         col = len(grid[0])
#         result = 0
#         def dfs(i, j, value):
#             # check if i and j are in the range since recursive calls can increment the value by 1 we want to make sure that it lies within the range
#             # convert 0s to 1
#             if(0<=i<rows and 0<=j<col and grid[i][j] == 0):
#                 grid[i][j] = value 
#                 dfs(i, j+1, value)
#                 dfs(i+1, j, value)
#                 dfs(i, j-1, value)
#                 dfs(i-1, j, value)
#         for i in range(rows):
#             for j in range(col):
#                 # flood fill technique
#                 # eliminate the 0's which are either in the first row, first column, last row, last column
#                 if(i==0 or j==0 or i==rows-1 or j==col-1):
#                     dfs(i, j, 1) 
                          
#         for i in range(rows):
#             for j in range(col):
#                 if(grid[i][j] == 0):
#                     dfs(i, j, 1) # traverse through all the nodes that are currently 0 and mark them as 1 (visited) hence there is a check for grid[i][j] == 0
#                     result+=1 # THE REMAINING ILSANDS MUST BE CLOSED - COUNT THEM
#         return result

class Solution(object):
    def maxAreaOfIsland(self, grid):
        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + area(r+1, c) + area(r-1, c) +
                    area(r, c-1) + area(r, c+1))

        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))

# print(isClosed &= False)
s = Solution()
grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
print(s.closedIsland(grid))
