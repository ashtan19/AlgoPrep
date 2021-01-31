"""
Leetcode: 987. Vertical Order Traversal of a Binary Tree

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(NlogN)
Space Complexity: O(n)

Pattern: Btree Traversal 
Technique: Traverse in DFS manner. Have a two layer dict that tracks col, row
            Then sort the col, then sort the rows in the cols, then sort the nodes in 
            each col, row

Problems Encountered:
Other Solutions: Partition Sorting

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        cur_row, cur_col = 0, 0
        stack = [(root, 0, 0)]
        result = []

        coords = defaultdict(lambda: defaultdict(list))

        while stack:
            node, col, row = stack.pop()
            coords[col][row].append(node.val)
            if node.left:
                stack.append((node.left, col-1, row+1))
            if node.right:
                stack.append((node.right, col+1, row+1))

        cols = sorted(coords.keys())

        for c in cols:
            col_result = []
            rows = sorted(coords[c].keys())
            for r in rows:
                col_result += sorted(coords[c][r])
            result.append(col_result)

        return result
