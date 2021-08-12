class Solution:
    def numSplits(self, word):
        ans = 0
        leftset = set()
        rightset = set(word)
        lastAppeared = {}
        for i in range(len(word)-1, -1,-1):
            if word[i] not in lastAppeared:
                lastAppeared[word[i]] = i
        i = 0
        while i< len(word):
            leftset.add(word[i])
            # if i has crossed the lastAppeared index it means that it does not exist in the right set and hence can be removed from the sets
            if(i>= lastAppeared[word[i]]):
                rightset.remove(word[i]) 
            if(len(leftset) == len(rightset)):
                ans+=1
            i+=1
        return ans

s = Solution()
print(s.numSplits("aacaba"))




