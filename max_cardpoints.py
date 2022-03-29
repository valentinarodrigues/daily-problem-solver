import math
# Bruteforce
'''
class Solution:
    def maxScore(self, cardPoints, k):
        ans =  -math.inf
        for i in range(k+1):
            ans = max(sum(cardPoints[:k-i] + cardPoints[-1: -i-1: -1]), ans)
        return ans
'''

# class Solution:
#     def maxScore(self, cardPoints, k):
#         startScore = 0
#         endPoints = 0
#         for i in range(k):
#             startScore +=cardPoints[i]

#         maxPoints = startScore
#         n = len(cardPoints)
#         for i in range(k-1, -1, -1):
#             startScore-=cardPoints[i]
#             endPoints += cardPoints[n-(k-i)]
#             currentScore = startScore+endPoints
#             maxPoints = max(currentScore, maxPoints)
#         return maxPoints


# class Solution:
#     def maxScore(self, cardPoints, k):
#         n = len(cardPoints)
#         requiredLength = n-k
#         maxPoints = sum(cardPoints)
#         minPoints = maxPoints 
#         startIndex = 0
#         arrayScore = 0
#         if(n == k):
#             return maxPoints
#         for i in range(n):
#             minSubArrayLength = i+1-startIndex
#             arrayScore += cardPoints[i]
#             if(minSubArrayLength == requiredLength):
#                 minPoints = min(minPoints, arrayScore)
#                 arrayScore -= cardPoints[startIndex]
#                 startIndex+=1
#         return maxPoints - minPoints


class Solution:
    def maxScore(self, arr, k):
        n = len(arr)
        if(n ==k):
            return sum(arr)
        maxScore = sum(arr[n-k:])
        startScore = maxScore
        for i in range(k):
            startScore += arr[i]
            startScore -= arr[n-k+i]
            if startScore>maxScore:
                maxScore = startScore
        return maxScore
s = Solution()
print(s.maxScore([100,40,17,9,73,75], 3))
# print(s.maxScore([1,2,3,4,5,6,1], 3))