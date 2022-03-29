from collections import defaultdict
class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):
        children = defaultdict(list)
        for i, m in enumerate(manager):
            if m >= 0: children[m].append(i)
        for i in children:
            print(i, children[i])

        def dfs(i):
            # find the max since one employee can manage a heirachy whereas other manager can just manage one employee under him
            '''
                    A
                   / \
                  B   C
                     / \
                    D   E   
            '''
            '''
            [0] is to manage case where the employee does not have to manage other employees i.e leaf node would be [] but max function dies not accept empty list
            '''
            return max([dfs(j) for j in children[i]] or [0]) + informTime[i]
        return dfs(headID)

s = Solution()

# n = 7
# headID = 6
# manager = [1,2,3,4,5,6,-1]
# informTime = [0,6,5,4,3,2,1]
n = 15
headID = 0
manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
# print(s.numOfMinutes(n, headID, manager, informTime))

n = 4
headID = 2
manager = [3,3,-1,2]
informTime = [0,0,162,914]
print(s.numOfMinutes(n, headID, manager, informTime))
