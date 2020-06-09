# Leetcode: 236. Lowest Common Ancestor of a Binary Tree

# Attempts: 1
# Completed: Y
# Acheived Ideal:

# Time Complexity: O(n)
# Space Complexity: O(n)

# Solving process:
# Problems Encountered:

# Other Solutions: Can use a stack


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        qpath, ppath = [], []
        self.dfs(root, q, qpath)
        self.dfs(root, p, ppath)
        curq = len(qpath)-1
        curp = len(ppath)-1
        while curq >= 0 and curp >= 0:
            if qpath[curq] != ppath[curp]:
                return qpath[curq+1]
            curq -= 1
            curp -= 1
        return qpath[curq+1]

    def dfs(self, root, nodeval, arr):

        if root:
            if root == nodeval:
                arr.append(root)
                return True

            if self.dfs(root.right, nodeval, arr) == True:
                arr.append(root)
                return True
            elif self.dfs(root.left, nodeval, arr) == True:
                arr.append(root)
                return True

            else:
                return False

        return False
