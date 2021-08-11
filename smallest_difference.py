import heapq


'''

Given an array nums, you are allowed to choose one element of nums and change it by any value in one move.

Return the minimum difference between the largest and smallest value of nums after perfoming at most 3 moves.

Example 1:

Input: nums = [5,3,2,4]
Output: 0
Explanation: Change the array [5,3,2,4] to [2,2,2,2].
The difference between the maximum and minimum is 2-2 = 0.
Example 2:

Input: nums = [1,5,0,10,14]
Output: 1
Explanation: Change the array [1,5,0,10,14] to [1,1,0,1,1]. 
The difference between the maximum and minimum is 1-0 = 1.
Example 3:

Input: nums = [6,6,0,1,1,4,6]
Output: 2
'''

'''
Since 3 possible moves

we can consider 
1. all 3 max values
2. all 3 min values
3. 2 min 1 max
4. 1 min 2 max
'''
class Solution:
    def minDifference(self, A):
        print(heapq.nsmallest(4, A))
        print(heapq.nlargest(4, A))
        return min(a - b for a,b in zip(heapq.nlargest(4, A), heapq.nsmallest(4, A)[::-1]))

s = Solution()
print(s.minDifference([6,6,0,1,1,4,6]))
[0, 1, 1, 4, 6, 6, 6 ]











