# order and str are strings composed of lowercase letters. In order, no letter occurs more than once.

# order was sorted in some custom order previously. We want to permute the characters of str so that they match the order that order was sorted. More specifically, if x occurs before y in order, then x should occur before y in the returned string.

# Return any permutation of str (as a string) that satisfies this property.

# Example:
# Input: 
# order = "cba"
# str = "abcd"
# Output: "cbad"
# Explanation: 
# "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
# Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

class Solution:
    def customSortString(self, order: str, word: str) -> str:
        result = []
        wt = {}
        newresult = []
        for o in range(len(order)):
            wt[order[o]] = o            
        for s in word:
            if(s not in order):
                result.append(s)
            else:
                newresult.append(wt[s])
                
        newresult.sort()
        for v in newresult:
            result.append(order[v]) 
                        
        return ''.join(result)
        
s = Solution()
print(s.customSortString("kqep", "pekeq"))

# optimized
class Solution:
    def customSortString(self, order: str, words: str) -> str:
        frequency = dict()
        for i in range(len(order)):
            frequency[order[i]] = 0
        trash = ''
        for word in words:
            if word in order:
                frequency[word]+=1
            else:
                trash += word
        result = ''
        for letter in order:
            result += frequency[letter]*letter
        result += trash
        return result