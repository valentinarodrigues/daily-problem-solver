class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Traversal:
    def in_order(self, root):
        # Left Root Right
        if root:
            self.in_order(root.left)
            print(root.value)
            self.in_order(root.right)

    def pre_order(self, root):
        # Root Left Right
        if root:
            print(root.value)
            self.pre_order(root.left)
            self.pre_order(root.right)

    def post_order(self, root):
        # Left right root
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.value)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
t = Traversal()
print(t.pre_order(root))
print('#################')
print(t.in_order(root))
print('#################')
print(t.post_order(root))
