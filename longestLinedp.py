class Solution:
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        
        if len(M) == 0:
            return 0
        
        dp = [[ [0, 0, 0, 0] for j in range(len(M[0]))] for i in range(len(M))]
        max_len = 0
        for row in range(len(M)):
            for col in range(len(M[0])):
                if M[row][col] == 1:
                    dp[row][col][0] = dp[row][col-1][0] + 1 if col > 0 else 1
                    dp[row][col][1] = dp[row-1][col][1] + 1 if row > 0 else 1
                    dp[row][col][2] = dp[row-1][col-1][2] + 1 if row > 0 and col > 0 else 1
                    dp[row][col][3] = dp[row-1][col+1][3] + 1 if row > 0 and col < len(M[0])-1 else 1

                max_len = max(max_len, dp[row][col][0], dp[row][col][1], dp[row][col][2], dp[row][col][3])
                
        return max_len
                    