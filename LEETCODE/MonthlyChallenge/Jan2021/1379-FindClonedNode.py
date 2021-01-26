"""
Leetcode: 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree

Attempts: 1
Completed: Y
Acheived Ideal: N
Under 30 Mins: Y

Time Complexity: O(n)
Space Complexity: O(n) if BFS. Could be O(h) if dfs

Pattern: BTree Traversal
Technique: DFS or BFS. DFS better b/c of better space

Problems Encountered:
Other Solutions:

"""

# BFS solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """

        from collections import deque

        o_queue = deque([original])
        c_queue = deque([cloned])

        while o_queue:
            level = len(o_queue)
            for i in range(level):
                o_node = o_queue.popleft()
                c_node = c_queue.popleft()

                if o_node == target:
                    return c_node
                if o_node.left:
                    o_queue.append(o_node.left)
                    c_queue.append(c_node.left)
                if o_node.right:
                    o_queue.append(o_node.right)
                    c_queue.append(c_node.right)


# DFS solution
class Solution:
    def getTargetCopy(self, original, cloned, target):
        stack_o, stack_c = [], []

        node_o, node_c = original, cloned

        while stack_o or node_o:
            while node_o:
                stack_o.append(node_o)
                stack_c.append(node_c)
                node_o = node_o.left
                node_c = node_c.left

            node_o = stack_o.pop()
            node_c = stack_c.pop()

            if node_o == target:
                return node_c

            node_o = node_o.right
            node_c = node_c.right

# DFS recursive


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def inorder(o: TreeNode, c: TreeNode):
            if o:
                inorder(o.left, c.left)
                if o is target:
                    self.ans = c
                inorder(o.right, c.right)

        inorder(original, cloned)
        return self.ans
