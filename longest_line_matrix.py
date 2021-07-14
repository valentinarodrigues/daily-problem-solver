class Solution:
  def  longestLine([][] M):
    if (M.length == 0) return 0
     ones = 0
    [][] dp = new [M[0].length][4]
    for ( i = 0; i < M.length; i+=1):
       old = 0;
      for ( j = 0; j < M[0].length; j+=1):
        if (M[i][j] == 1):
          dp[j][0] = dp[j - 1][0] + 1 if  j > 0 else 1;
          dp[j][1] = dp[j][1] + 1  if i > 0 else 1;
           prev = dp[j][2];
          dp[j][2] =  old + 1 if (i > 0 and j > 0) else 1;
          old = prev;
          dp[j][3] =  dp[j + 1][3] + 1 if  (i > 0 and j < M[0].length - 1) else 1;
          ones =
              max(ones, dp[j][0], dp[j][1]), dp[j][2], dp[j][3]);
        else:
            old = dp[j][2];
            dp[j][0] = dp[j][1] = dp[j][2] = dp[j][3] = 0;

    return ones;
