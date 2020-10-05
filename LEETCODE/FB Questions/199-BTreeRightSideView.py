"""
Leetcode: 199. Binary Tree Right Side View

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(n)
Space Complexity: O(H)

Pattern: Tree Traversal 
Technique: Recursion or Iterative with stack

Problems Encountered:
Other Solutions: Can also do BFS

"""


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def checkRightSide(node, depth, result):
            if node:
                if depth >= len(result):
                    result.append(node.val)
                if node.right:
                    checkRightSide(node.right, depth+1, result)
                if node.left:
                    checkRightSide(node.left, depth+1, result)
        result = []
        checkRightSide(root, 0, result)
        return result
