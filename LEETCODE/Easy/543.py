# Leetcode: 543 Diameter of Binary Tree

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


# Leetcode Solution:
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 1

        def depth(node):
            if not node:
                return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1
