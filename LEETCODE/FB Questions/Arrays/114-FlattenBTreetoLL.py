"""
Leetcode: 114. Flatten Binary Tree to Linked List

Attempts: 1
Completed: Y
Acheived Ideal: N 
Under 30 Mins: Y

Time Complexity: O(n)
Space Complexity: O(n) but can be O(1) without recursion

Pattern: Binary Tree
Technique: Recursion or Morris Traversal for O(1) Space

Problems Encountered: Forgot to set left child to None 
Other Solutions: Morris Traversal 

"""


# Recursion Solution - Very fast but O(n) space
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def recursive_flatten(root):
            if not root.left and not root.right:
                return root
            last_left, last_right = root, root
            temp_right = root.right
            if root.left:
                last_left = recursive_flatten(root.left)
                root.right = root.left
                root.left = None
                last_right = last_left
            if temp_right:
                last_right = recursive_flatten(temp_right)
                last_left.right = temp_right
            return last_right
        if root:
            last_right = recursive_flatten(root)
        return


# Iterative Morris Traversal Solution
class Solution:

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # Handle the null scenario
        if not root:
            return None

        node = root
        while node:

            # If the node has a left child
            if node.left:

                # Find the rightmost node
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right

                # rewire the connections
                rightmost.right = node.right
                node.right = node.left
                node.left = None

            # move on to the right side of the tree
            node = node.right
