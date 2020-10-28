from collections import deque

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def check_mirror(level):
    l, r = 0, len(level)-1
    while l < r:
        if level[l] != level[r]:
            return False
        l += 1
        r -= 1
    return True


def symmetricTree(root):
    if root is None:
        return True

    dq = deque()
    dq.append(root)

    while dq:
        level_size = len(dq)
        level = []
        for i in range(level_size):
            curr_node = dq.popLeft()
            level.append(curr_node.val)
            if curr_node.left:
                dq.append(curr_node.left)
            if curr_node.right:
                dq.append(curr_node.right)

        if check_mirror(level) == False:
            return False

    return True


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(symmetricTree(root))
