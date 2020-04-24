# Definition for a binary tree node.
# First Method: O(n^2)
# Problem is that getheight is called over and over as you get deeper into the tree

# Second Method O(n)
# Create a height object that is passed and incremented as you go deeper into the tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def isBalanced(self, root):
#         if root is None: return True

#         heightDiff = self.getHeight(root.left) - self.getHeight(root.right)
#         if (abs(heightDiff) <= 1) and self.isBalanced(root.left) is True and self.isBalanced(root.right) is True: 
#             return True
#         else:
#             return False

    
#     def getHeight(self, root):
#         if root is None: return 0
#         return max(self.getHeight(root.left), self.getHeight(root.right)) + 1

class Height: 
    def __init__(self):
        self.height = 0

class Solution:

    def isBalanced(self, root, height):
        lheight = Height()
        rheight = Height()
        
        if root is None: 
            return True
        
        left = self.isBalanced(root.left, lheight)
        right = self.isBalanced(root.right, rheight)

        height.height = max(lheight.height, rheight.height) + 1 # As you traverse deeper into the tree, you will continue to increase the original height

        if abs(lheight.height - rheight.height) <= 1:
            return left and right
        else:
            return False



testTree = TreeNode(1)
testTree.left = TreeNode(2)
testTree.right = TreeNode(3)
testTree.left.left = TreeNode(4)
testTree.left.left.left = TreeNode(5)
testSolution = Solution()
testHeight = Height()
print(testSolution.isBalanced(testTree,testHeight))