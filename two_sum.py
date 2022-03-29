class Solution:
    def twoSum(self, nums, target: int):
        mapping = {}
        for idx, num in enumerate(nums):
            f = target - num 
            if(f in mapping):
                return[mapping[f], idx]   
            mapping[num] = idx
        return []
            
        
            
s = Solution()
print(s.twoSum([3,2,4], 6))
