class Solution:
    def carFleet(self, target, pos, speed):
        # sort the array based on position
        # calculate time taken to reach the target for each car at the position
        # time = distance/speed
        time = [float(target-p)/s for p,s in sorted(zip(pos, speed))]
        current = 0
        result = 0
        # reverse the array so as to get the array in the array with the time to arrive first to begin with 
        for t in time[::-1]:
            # if the next car has time more than the previous it means it wont collide and reach the target
            # wont collide means a new fleet and if it collides it means part of the same fleet
            if(t>current):
                result+= 1
                current = t
        return result

s = Solution()
pos = [10,8,0,5,3]
speed = [2,4,1,1,3]
target = 12 
print(s.carFleet(target, pos, speed))