from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_count = Counter(secret)
        guess_count = Counter(guess)
        cows = len(secret) - sum((guess_count - secret_count).values())
        bulls = sum([1 for i in range(len(secret)) if secret[i] == guess[i]])
        cows = cows - bulls
        return f'{bulls}A{cows}B'

# from collections import defaultdict
# class Solution:
#     def getHint(self, secret: str, guess: str) -> str:
#         # cows = check if number of elements in guess is present in secret
#         # bulls = count of position match

#         num_dict = defaultdict(int)
#         cows = 0
#         bulls = 0
#         for c in range(len(secret)):
#             if secret[c] == guess[c]:
#                 bulls+=1
#             else:
#                 num_dict[secret[c]] += 1
#                 num_dict[guess[c]] -=1 
#         for num in num_dict:
#             if(int(num_dict[num])>0):
#                 cows+= int(num_dict[num])
#         cows = len(secret) - bulls - cows
#         return '{}A{}B'.format(bulls,cows)
#         print('{}A{}B'.format(bulls,cows))
#         print(bulls, num_dict)

s = Solution()
print(s.getHint(secret='1123', guess='0111'))

# Example 1:
# Input: secret = "1807", guess = "7810"
# Output: "1A3B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1807"
#   |
# "7810"
# Example 2:

# Input: secret = "1123", guess = "0111"
# Output: "1A1B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1123"        "1123"
#   |      or     |
# "0111"        "0111"
# Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
# Example 3:

# Input: secret = "1", guess = "0"
# Output: "0A0B"
# Example 4:

# Input: secret = "1", guess = "1"
# Output: "1A0B"