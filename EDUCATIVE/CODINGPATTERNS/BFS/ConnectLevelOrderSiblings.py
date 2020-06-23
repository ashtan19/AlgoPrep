'''
Question: Connect Level Order Siblings (medium)

Time Complexity: O(n)
Space Complexity: O(n)

Pattern: BFS
Technique: 


'''


from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # level order traversal using 'next' pointer
    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()


def connect_level_order_siblings(root):
    # TODO: Write your code here
    if root is None:
        return None
    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        prev_node = TreeNode(0)
        for _ in range(level_size):
            cur_node = queue.popleft()
            prev_node.next = cur_node
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
            prev_node = prev_node.next
    return
