
class Solution:
    def closedIsland(self, grid) -> int:
        rows = len(grid)
        col = len(grid[0])
        result = 0
        def dfs(i, j, value):
            # check if i and j are in the range since recursive calls can increment the value by 1 we want to make sure that it lies within the range
            # convert 0s to 1
            if(0<=i<rows and 0<=j<col and grid[i][j] == 0):
                grid[i][j] = value 
                dfs(i, j+1, value)
                dfs(i+1, j, value)
                dfs(i, j-1, value)
                dfs(i-1, j, value)
        for i in range(rows):
            for j in range(col):
                # flood fill technique
                # eliminate the 0's which are either in the first row, first column, last row, last column
                if(i==0 or j==0 or i==rows-1 or j==col-1):
                    dfs(i, j, 1) 
                          
        for i in range(rows):
            for j in range(col):
                if(grid[i][j] == 0):
                    dfs(i, j, 1) # traverse through all the nodes that are currently 0 and mark them as 1 (visited) hence there is a check for grid[i][j] == 0
                    result+=1 # THE REMAINING ILSANDS MUST BE CLOSED - COUNT THEM
        return result



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
