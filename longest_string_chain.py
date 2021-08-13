from collections import defaultdict
class Solution:
    def longestStrChain(self, words) -> int:
        mem = {}
        result = 1 # the word itself needs to be considered
        for word in sorted(words, key =len):
            mem[word] = 1 # including the length of the word itself
            for w in range(len(word)):
                prev = word[:w] + word[w+1:] # prev formed by eliminating one character at a time in the current word
                if prev in mem:
                    mem[word] = mem[prev] + 1
                    result = max(mem[word], result)
        return result
input = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
s = Solution()
print(s.longestStrChain(input))

# example 
# ["xbc","pcxbcf","xb","cxbc","pcxbc"]
# sort ["xb", "xbc","cxbc","pcxbc", "pcxbcf"]

# ["xb", "xbc","cxbc","pcxbc", "pcxbcf"]


# mem["xb"] = 1

# prev words would be [x, b] which do not exist so go to next word

# xbc
# prev words would be [xb, xc, bc]

# we have memoised value of xb so we add the memoised to the current  value 1
# mem["xbc"] = mem["xb"] + 1
