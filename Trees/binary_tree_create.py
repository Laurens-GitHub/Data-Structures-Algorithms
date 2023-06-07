# Code
# 1. Node Class
#     - Data (string)
#     - Left (Node)
#     - Right (Node)

from typing import List
class Node:
    def __init__(self, data: str, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def getData(self):
        return self.data

    def setLeft(self, left):
        self.left = left

    def getLeft(self):
        return self.left

    def setRight(self, right):
        self.right = right

    def getRight(self):
        return self.right

# 2. MakeTree(inorder, preorder)
# ```
# MakeTree(inorder, preorder)
#     root = preorder[0]

#     root.left = MakeTree(.....)
#     root.right = MakeTree(......)

#     return root
# ```

def makeTree(inorder: List[str], preorder: List[str]):

    root = Node(preorder[0]) # root is a node, and the data is the first item in preorder list

    if len(preorder) == 1:
        return root

    root_index = inorder.index(root.getData())

    left_inorder = []
    if root_index != 0:
        left_inorder = inorder[0:root_index]
        left_preorder = preorder[1: len(left_inorder) + 1]
        root.setLeft(makeTree(left_inorder, left_preorder))

    if root_index != len(inorder) - 1:
        right_inorder = inorder[root_index:]
        right_preorder = preorder[len(left_inorder)+1:]
        root.setRight(makeTree(right_inorder, right_preorder))

    return root

# 3. Print in order
# ```
# PrintInOrder(root)
#     if root is None return
#     PrintInOrder(root.left)
#     print(root.data)
#     PrintInOrder(root.right)
# ```

def printInOrder(root: Node):
    if root is None: return

    printInOrder(root.getLeft())
    print(root.getData(), end = " ")
    printInOrder(root.getRight())


# 4. Print Pre Order
# ```
# PrintPreOrder(root)
#     if root is None return
#     print(root.data)
#     PrintPreOrder(root.left)
#     PrintPreOrder(root.right)
# ```

def printPreOrder(root: Node):
    if root is None: return

    print(root.getData(), end = " ")
    printPreOrder(root.getLeft())
    printPreOrder(root.getRight())

# 5. Print Post Order
# ```
# printPostOrder(root)
#     if root is None return
#     PrintPostOrder(root.left)
#     PrintPostOrder(root.right)
#     print(root.data)
# ```

def printPostOrder(root: Node):
    if root is None: return

    printPostOrder(root.getLeft())
    printPostOrder(root.getRight())
    print(root.getData(), end = " ")

def main():
    root = makeTree(["D", "B", "E", "A", "F", "C"], ["A", "B", "D", "E", "C", "F"])
    printPreOrder(root)
    print()
    printInOrder(root)
    print()
    printPostOrder(root)
    print()

if __name__ == "__main__":
    main()

inorder1 = "A B D F E R".split(" ")
# test if functions work with edge cases
# Tree levels
# A
# B C
# D E F
