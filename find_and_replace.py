class Solution:
    def findReplaceString(self, s: str, indices, sources, targets) -> str:
        #         isn't it because if you do it from left to right, the index will be overwritten after you replace the previous one. e.g.

        # S = ""abcd
        # indexes = [0,2]
        # sources = ["a", "cd"]
        # targets = ["eeee", "ffff"]
        # after first iteration, the S becomes eeeebcd and if you look for index at 2 now, it is e won't match cd
        for i, s ,t in sorted(zip(indices, sources, targets), reverse =True):
            # new string = old string just before the index where the string needs to be replaced (end index is not counted) + new replacement 
            # + S[i+len(s):] => index starting from the point where old string is replaced
            # i+len(s) => number of characters in source to be replaced
            S = S[:i] + t + S[i+len(s):] if(S[i:i+len(s)]) == s else S
        return S        