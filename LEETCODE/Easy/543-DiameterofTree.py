# Leetcode: 543 Diameter of Binary Tree

# Attempts: 2

# Time Complexity: O(n)
# Space Complexity: O(1) -> Need to double Check
# Solving process:
# Problems Encountered:

# Other Solutions:


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        height, maxD = self.findHeightandD(root)
        return maxD

    def findHeightandD(self, root):
        if root == None:
            return 0, 0

        lH, lD = self.findHeightandD(root.left)
        rH, rD = self.findHeightandD(root.right)

        curD = lH + rH
        maxD = max(curD, lD, rD)
        height = max(lH, rH) + 1

        return height, maxD

# Attempt 2


class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.result = 0
        self.depthofnode(root)
        return self.result

    def depthofnode(self, node):
        if node:
            left = self.depthofnode(node.left)
            right = self.depthofnode(node.right)
            self.result = max(self.result, left + right)
            return max(left, right) + 1
        else:
            return 0
