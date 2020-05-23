# Leetcode: 102 Binary Tree Level Order Traversal

# Completed: Y
# Acheived Ideal: Y

# Time Complexity: O(n)
# Space Complexity: O(n)

# Solving process:
# Problems Encountered:

# Other Solutions: Use a Queue


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root == None:
            return None
        level = 0
        hashtable = {0: [root]}

        while level in hashtable:
            for i in range(len(hashtable[level])):
                if hashtable[level][i].left:
                    if level+1 in hashtable:
                        hashtable[level+1].append(hashtable[level][i].left)
                    else:
                        hashtable[level+1] = [hashtable[level][i].left]
                if hashtable[level][i].right:
                    if level+1 in hashtable:
                        hashtable[level+1].append(hashtable[level][i].right)
                    else:
                        hashtable[level+1] = [hashtable[level][i].right]

                hashtable[level][i] = hashtable[level][i].val
            level += 1

        return hashtable.values()

# Cleaner Solution but same Idea


def levelOrder(self, root):
    if not root:
        return []
    ans, level = [], [root]
    while level:
        ans.append([node.val for node in level])
        temp = []
        for node in level:
            temp.extend([node.left, node.right])
        level = [leaf for leaf in temp if leaf]
    return ans
