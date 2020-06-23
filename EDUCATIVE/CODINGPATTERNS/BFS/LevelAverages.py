'''
Question: Level Averages in a Binary Tree (easy)

Time Complexity: O(n)
Space Complexity: O(n)

Pattern: BFS
Technique: Just average instead of recording the elements


'''


from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root):
    result = []
    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        level_sum = 0.0
        for _ in range(level_size):
            cur_node = queue.popleft()
            level_sum += cur_node.val
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        result.append(float(level_sum)/level_size)
    # TODO: Write your code here
    return result
