class Solution:
    def carFleet(self, target, pos, speed):
        time = [float(target-p)/s for p,s in sorted(zip(pos, speed))]
        current = 0
        result = 0
        for t in time[::-1]:
            if(t>current):
                result+= 1
                current = t
        return result

s = Solution()
pos = [10,8,0,5,3]
speed = [2,4,1,1,3]
target = 12 
print(s.carFleet(target, pos, speed))