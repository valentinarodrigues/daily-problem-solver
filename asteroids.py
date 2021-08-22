# Example 1:
# Input: asteroids = [5,10,-11]
# Output: [-11]
# Explanation: The 10 and -11 collide resulting in -11. The 5 and -11 collide resulting in -11.

# Example 2:
# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.

# Example 3:
# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

# Example 4:
# Input: asteroids = [-2,-1,1,2]
# Output: [-2,-1,1,2]
# Explanation: The -2 and -1 are moving left, while the 1 and 2 are moving right. Asteroids moving the same direction never meet, so no asteroids will meet each other.


class Solution(object):
    def asteroidCollision(self, asteroids):
        ans = []
        for asteroid in asteroids:
            # observe use of while else
            while ans and asteroid< 0 <ans[-1]:
                if(ans[-1]<-asteroid):
                    ans.pop()
                    continue 3 # keep popping if the next asteroid also collides
                elif -asteroid == ans[-1]:
                    ans.pop()
                break
            else:
                ans.append(asteroid)
        return ans