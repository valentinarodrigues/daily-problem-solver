def maxPoints(points):
    rows = len(points)
    cols = len(points[0])
    dp = points[0]
    left = [0] * cols
    right = [0] * cols
    for i in range(1, rows):
        for j in range(cols):
            if(j == 0):
                left[j] = dp[j]
            else:
                left[j] = max(dp[j],left[j-1] -1 )
        for j in range(cols-1, -1, -1):
            if(j == cols-1):
                right[j] = dp[j]
            else:
                right[j] = max(dp[j], right[j+1] -1)
        for j in range(cols):
            dp[j] = points[i][j] + max(left[j], right[j])
    return max(dp)

# print(maxPoints([[1,2,3],[1,5,1],[3,1,1]]))

print(maxPoints([[1,5],[2,3],[4,2]]))