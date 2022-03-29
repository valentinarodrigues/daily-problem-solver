class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        char_set = set()
        left = 0
        for right, char in enumerate(s):
            while (char in char_set):
                char_set.remove(s[left])
                left+=1
            char_set.add(char)
            res=max(res, right-left+1)
        return res
        
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.