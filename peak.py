
class SolutionOptimised:
    def findPeakElement(self, nums) -> int:
        return search(nums, 0, nums.length - 1)

    def search(nums, l, r):
        if(l == r):
            return l
        mid = (l+r)/2
        if(nums[mid]>nums[mid+1]):
            return search(nums, l, mid)
        return search(nums, mid+1, r)



import math
class Solution:
    def findPeakElement(self, nums) -> int:
        # save the peek 
        # save the peekindex => this is for the result
        total_length = (len(nums))
        number_of_elements = total_length//2+1
        total_length-=1
        peakIndex = -1
        for i in range(number_of_elements):
            if(nums[i]>nums[total_length]):
                if(nums[i]>nums[peakIndex]):
                    peakIndex = i
            elif nums[total_length] >= nums[i]:
                if(nums[total_length]>=nums[peakIndex]):
                    peakIndex = total_length
            total_length-=1
        if(peakIndex==-1):
            return 0
        return peakIndex
            
s = Solution()
print(s.findPeakElement([1,2,1]))