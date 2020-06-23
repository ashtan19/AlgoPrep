'''
Question: Reverse Level order Traversal

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: BFS
Technique: Difference is that you appendLeft to the result


'''


def traverse(root):
    result = deque()
    if root is None:
        return result
    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        currentLevel = []
        for _ in range(level_size):
            cur_node = queue.popleft()
            currentLevel.append(cur_node.val)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        result.appendleft(currentLevel)

    return result
