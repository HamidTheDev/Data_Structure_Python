#binary tree node class
class TreeNode:
 def __init__(self, data):
  self.data = data
  self.left = None
  self.right = None

#creating node with node class
rootNode = TreeNode(5)
node2 = TreeNode(10)
node3 = TreeNode(20)

#linking node with each other
rootNode.left = node2
rootNode.right = node3

#printing binary tree
def printTree(root):
 if root is 
