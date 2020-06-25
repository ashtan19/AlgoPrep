'''
Question: Binary Tree Path Sum (easy)

Time Complexity: O(n)
Space Complexity: O(n) -> if Tree is a LL

Pattern: DFS
Technique: 


'''


# Recursive Solution
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, sum):
    # TODO: Write your code here
    return DFS(root, sum, 0)


def DFS(root, sum, cur_sum):
    if root == None:
        return False
    if not root.left and not root.right:
        return cur_sum + root.val == sum
    cur_sum += root.val
    return DFS(root.left, sum, cur_sum) or DFS(root.right, sum, cur_sum)

# Provided Solution


def has_path(root, sum):
    if root is None:
        return False

    # if the current node is a leaf and its value is equal to the sum, we've found a path
    if root.val == sum and root.left is None and root.right is None:
        return True

    # recursively call to traverse the left and right sub-tree
    # return true if any of the two recursive call return true
    return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)
