class Solution(object):
    def numMatchingSubseq(self, S, words):
        ans = 0
        res = [[] for i in range(26)]
        for word in words:
            w = iter(word)
            res[ord(next(w))-ord('a')].append(w)
        # 0 a, acd, ace
        # 1 bb
        # when I use next the next time, the next letter will be accessible

        
        for char in S:
            result = res[ord(char)-ord('a')] 
            res[ord(char)-ord('a')]  = []
            while(result):
                lastElement = result.pop()
                
                nxt = next(lastElement, None)
                print('nxt', nxt)
                if nxt:
                    res[ord(nxt)-ord('a')].append(lastElement)
                else:
                    ans+=1
                
            
        return ans
# [0] a, acd, ace 
# [1] bb             

s = Solution()
S = "abcde"
words = ["a","bb","acd","ace"]
print(s.numMatchingSubseq(S, words))
