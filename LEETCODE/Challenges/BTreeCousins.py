# Leetcode: Challenge Question Cousins in Binary Tree

# Time Complexity: O(n)
# Space Complexity: 
# Solving process:
# Problems Encountered: 

# Other Solutions:



# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

# Return true if and only if the nodes corresponding to the values x and y are cousins.

 

# Example 1:


# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
# Example 2:


# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
# Example 3:



# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
 

# Note:

# The number of nodes in the tree will be between 2 and 100.
# Each node has a unique integer value from 1 to 100.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root.val == x or root.val == y:
            return False
        xHeight, xParent = self.findNodeHeightandParent(root, x, 0)
        yHeight, yParent = self.findNodeHeightandParent(root, y, 0)
        if xHeight != yHeight or xParent == yParent:
            return False
        else: 
            return True
        
     
    def findNodeHeightandParent(self, tree, node, height):
        if tree.left == None and tree.right == None:
            return None, None
        if tree.left:
            if tree.left.val == node:
                return height + 1, tree
            else:
                leftHeight, leftParent = self.findNodeHeightandParent(tree.left, node, height+1)
                if leftHeight != None: return leftHeight, leftParent
                
        
        if tree.right:
            if tree.right.val == node:
                return height + 1, tree
            else:
                rightHeight, rightParent = self.findNodeHeightandParent(tree.right, node, height+1)
                if rightHeight != None: return rightHeight, rightParent
            
        return None, None