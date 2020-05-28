# Leetcode: 105. Construct Binary Tree from Preorder and Inorder Traversal

# Completed: N
# Acheived Ideal:

# Time Complexity:
# Space Complexity:

# Solving process:
# Problems Encountered: Had Problems with popping preorder[0] b/c of O(n) time

# Other Solutions:



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root


# Build hashtable to get rid of preorder.pop[0] O(n) problem
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        inor_dict = {}
        for i, num in enumerate(inorder):
            inor_dict[num] = i
        pre_iter = iter(preorder)

        def helper(start, end):
            if start > end:
                return None
            root_val = next(pre_iter)
            root = TreeNode(root_val)
            idx = inor_dict[root_val]
            root.left = helper(start, idx-1)
            root.right = helper(idx+1, end)
            return root

        return helper(0, len(inorder) - 1)
