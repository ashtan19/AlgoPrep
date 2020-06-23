'''
Question: Minimum Depth of a Binary Tree (easy)

Time Complexity: O(n)
Space Complexity: O(n)

Pattern: BFS
Technique: Return depth when you find a leaf


'''


from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_minimum_depth(root):
    # TODO: Write your code here
    queue = deque()
    queue.append(root)
    depth = 0
    while queue:
        level_size = len(queue)
        depth += 1
        for _ in range(level_size):
            cur_node = queue.popleft()
            if cur_node.left == None and cur_node.right == None:
                return depth
            else:
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)

    return depth
