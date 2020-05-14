# Leetcode: 94 BTree Inorder Traversal Iteratively

# Time Complexity: O(n)
# Space Complexity: O(3n)
# Solving process:
# Problems Encountered:

# Other Solutions: Can also use a Morris Traversal => make parent right child of rightmost node of left child


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        stack = []
        isVisited = {}
        result = []

        stack.append(root)

        while stack != []:
            p = stack[-1]

            # Check if node is leaf
            if p.left == None and p.right == None:
                result.append(p.val)
                stack.pop()

            else:
                # Check if node has been visited. If yes go right
                if p in isVisited:
                    result.append(p.val)
                    stack.pop()
                    if p.right:
                        stack.append(p.right)
                else:
                    isVisited[p] = True

                    while p.left != None:
                        stack.append(p.left)
                        p = p.left
                        isVisited[p] = True
        return result

# iteratively - Cleaner Solution


def inorderTraversal(self, root):
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right
