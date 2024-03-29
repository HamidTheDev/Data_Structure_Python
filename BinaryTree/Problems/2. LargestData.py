#creating treenode
class TreeNode:
   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None
        

rootNode = TreeNode(10)
node2 = TreeNode(5)
node3 = TreeNode(3)

rootNode.left = node2
rootNode.right = node3

#logic: last most left and right node will return -1, -1 and we will find max of the node and -1, -1 like max(node, -1 -1) it will continue for all the node both left and right side
def largestData(root):
    if root is None:
        return -1
    leftLarge = largestData(root.left) #this is continuously call left side and start executing "largest = max(leftLarge, rightLarge, root.data)" this line by skipping "rightLarge = largestData(root.right)" and continue returning largest from each node
    rightLarge = largestData(root.right)
    largest = max(leftLarge, rightLarge, root.data)
    return largest

print(largestData(rootNode)) #10