class Solution():
    def longest_one(self, Matrix):
        if(len(M) == 0):
            return 0
        state = [[[0,0,0,0] for j in range(len(Matrix[0]))] for i in range(len(Matrix))]
        max_len = 0
        for row in range(len(Martrix)):
            for col in range(len(Matrix[0])):
                if(Matrix[i][j] == 1):
                    state[i][j][0] = dp[i][j-1][0] + 1 if j>0 else 1
                    state[i][j][1] = dp[i-1][j][1] + 1 if i>0 else 1
                    state[i][j][2] = dp[i-1][j-1][2] if i>0 and j>0 else 1
                    state[i][j][3] = dp[i-1][j+1][3] if i>0 and j<len(Matrix[0]) else 1
        
            max_len = max(state[i][j][0], state[i][j][1],state[i][j][2],state[i][j][3], max_len)
        return max_len