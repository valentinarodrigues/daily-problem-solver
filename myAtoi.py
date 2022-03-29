class Solution:
    def myAtoi(self, s: str) -> int:
        max_value =  2**31
        sign, i, base = 1, 0, 0
        if not len(s):
            return 0
        while i<len(s) and s[i] == ' ':
            i+=1
        if(i<len(s) and (s[i] == '+' or s[i] == '-')):
            sign =  1 - 2 * (s[i] =='-')
            i+=1
        while(i<len(s) and s[i]>='0' and s[i]<='9'):
            if(base > max_value//10) or ((base == max_value//10) and (s[i]) > '7'): # since calculate is done before
                if(sign == 1):
                    return max_value-1
                else:
                    return -max_value
            base = 10*base + (ord(s[i]) - ord('0'))
            i+=1
        return sign * base


 
     