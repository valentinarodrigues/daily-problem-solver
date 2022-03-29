class Solution(object):
    def minEatingSpeed(self, piles, H):
        # Can Koko eat all bananas in H hours with eating speed K?
        def possible(K):
            print('k', K)
            print('s', sum((((p-1)//K)+1 for p in piles)))
            print('s', sum((((p-1)//K)+1 for p in piles))<= H)
            return sum(((p-1) // K) + 1 for p in piles) <= H

        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            # if not possible(mi): # since this solution is not possible we take the next possible integer hence +1 
            #     lo = mi + 1
            # else: # since we want the minimum number k when k satisifies the condition we set it as the hi value since we want to cap the solution  
            #     hi = mi
            if(possible(mid)):
                hi = mid
            else:
                lo = mid+1
        return lo
s = Solution()
piles = [3,6,7,11]
h = 8
print(s.minEatingSpeed(piles, h))

