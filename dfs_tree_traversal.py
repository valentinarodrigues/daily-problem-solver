class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def inOrder(root):
    if(root):
        inOrder(root.left)    
        print(root.value)
        inOrder(root.right)

def preOrder(root):
    if root:
        print(root.value)
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.value)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

preOrder(root)
print('')
postOrder(root)
print('')
inOrder(root)