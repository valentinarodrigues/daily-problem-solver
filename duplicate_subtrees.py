class Solution:
    def findDuplicateSubtrees(self, root):
        def traverse(root):
            if not root: return "null"
            struct = str(root.val) + ',' + traverse(root.left) + ',' + traverse(root.right) # traverse the tree anyhow pre, post, in doesnt matter
            nodes[struct].append(root) 
            return struct
        
        nodes = defaultdict(list)
        traverse(root)
        return [nodes[struct][1] for struct in nodes if len(nodes[struct])>1]
        # if len(nodes[struct])>1 this condition says that if more than 1 subtree has different roots it means they are duplicate