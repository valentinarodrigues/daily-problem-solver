
class RLEIterator:
    
    def __init__(self, encoding):
        self.encoding = encoding
        self.idx = 0 # iterating over the frequency of the numbers i.e 3, 0 2 which gives the frequency of the next number in line rle[3, 8, 0, 9, 2, 5] 
        
    def next(self, n: int) -> int:
        while(self.idx<len(self.encoding)):
            if(n<=self.encoding[self.idx]):
                self.encoding[self.idx] -= n
                return self.encoding[self.idx+1]
            else:
                n-= self.encoding[self.idx]
                self.encoding[self.idx] = 0
                self.idx+=2
        return -1
                    
result = []

commands = ["RLEIterator", "next", "next", "next", "next"]
values = [[[3, 8, 0, 9, 2, 5]], [2], [1], [1], [2]]
# RLEIterator rLEIterator = new RLEIterator([3, 8, 0, 9, 2, 5]); 
# // This maps to the sequence [8,8,8,5,5].
# rLEIterator.next(2); // exhausts 2 terms of the sequence, returning 8. The remaining sequence is now [8, 5, 5].
# rLEIterator.next(1); // exhausts 1 term of the sequence, returning 8. The remaining sequence is now [5, 5].
# rLEIterator.next(1); // exhausts 1 term of the sequence, returning 5. The remaining sequence is now [5].
# rLEIterator.next(2); // exhausts 2 terms, returning -1. This is because the first term exhausted was 5,
# but the second term did not exist. Since the last term exhausted does not exist, we return -1.
for c,v in zip(commands, values):
    if(c == "RLEIterator"):
        # initialize array
        obj = RLEIterator(v[0])
        result.append(None)
    elif(c == "next"):
        key = v[0]
        result.append(obj.next(key))
print(result)
