class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Post order traversal
#         1
#     2        3
# 4       5 6     7
# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]

# Input: root = [1,2,4,null,3], to_delete = [3]
# Output: [[1,2,4]]
class Solution:
    resultList = []
    def delNodes(self, root: TreeNode, to_delete: [int]) -> [TreeNode]:
        self.resultList = []
        root = self.helper(root, to_delete)
        if root and root.val not in to_delete:
            self.resultList = [root] + self.resultList
        return self.resultList
    
    def helper(self, root: TreeNode, to_delete: [int]) -> TreeNode:
        if root == None:
            return None
        # traverse left 
        if root.left:
            root.left = self.helper(root.left, to_delete)
        if root.right:
            root.right = self.helper(root.right, to_delete)
            
        if root.val in to_delete:
            if root.left:
                self.resultList.append(root.left)
            if root.right:
                self.resultList.append(root.right)
            return None
        else:
            return root

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
for i in s.delNodes(root, [3,5]):
    print(i.val)