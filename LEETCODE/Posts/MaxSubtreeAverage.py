"""
Leetcode: Amazon | OA 2019 | Subtree with Maximum Average

Attempts: 1
Completed: N, but got the right idea and approach. Did not implement
Acheived Ideal:
Under 30 Mins: 

Time Complexity: O(n)
Space Complexity: O(h)

Pattern: Tree Recursion DFS 
Technique: Create a helper function that checks if a node is a valid subtree, calculate the sum of the 
            subtree and the number of elements in it. Update a global variable of maxaverage and which node

Problems Encountered:
Other Solutions:

"""


class TreeNode:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.dic = {}
        self.inordersum(root)
        return max(self.dic.items(), key=lambda x: x[1])[0]

    def inordersum(self, root):
        if root:
            total = root.val
            nodeCount = 1

            for child in root.children:
                childSum, childCount = self.inordersum(child)
                total += childSum
                nodeCount += childCount

            avg = (total)/(nodeCount)

            if nodeCount != 1:
                self.dic[root.val] = avg
            return [total, nodeCount]
        else:
            return [0, 0]


n4 = TreeNode(11, [])
n5 = TreeNode(2, [])
n6 = TreeNode(3, [])
n7 = TreeNode(15, [])
n8 = TreeNode(8, [])
n2 = TreeNode(12, [n4, n5, n6])
n3 = TreeNode(18, [n7, n8])
n1 = TreeNode(20, [n2, n3])
ss = Solution()
print(ss.maximumAverageSubtree(n1))
