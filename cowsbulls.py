from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        incorrectGuessing = defaultdict(int)
        incorrectGuesses = 0
        for idx, digit in enumerate(secret):
            if(digit == guess[idx]):
                bulls+=1
            else:
                incorrectGuessing[digit] += 1
                incorrectGuessing[guess[idx]] -=1
        for num in incorrectGuessing:
            if(incorrectGuessing[num]>0):
                incorrectGuesses = incorrectGuesses+incorrectGuessing[num]
        cows = len(secret) - bulls -incorrectGuesses
        return '{}A{}B'.format(bulls, cows)                
                
            