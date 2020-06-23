'''
Question: Level Order Traversal

Time Complexity: O(n)
Space Complexity: O(n)

Pattern: BFS
Technique: 1. Use a queue that stores (node and level) as a tuple and create / add
            to each level array 
            2. Take note of number of nodes in each level and process only that many nodes (putting
            them in the level array)


'''


def traverse(root):
    result = []
    queue = deque()
    queue.append((root, 0))
    # TODO: Write your code here
    cur_level = -1
    while len(queue) > 0:
        cur_node, node_level = queue.popleft()
        if node_level != cur_level:
            level_array = [cur_node.val]
            result.append(level_array)
            cur_level = node_level
        else:
            result[-1].append(cur_node.val)
        if cur_node.left:
            queue.append((cur_node.left, node_level + 1))
        if cur_node.right:
            queue.append((cur_node.right, node_level + 1))

    return result


def traverse(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        currentLevel = []
        for _ in range(levelSize):
            currentNode = queue.popleft()
            # add the node to the current level
            currentLevel.append(currentNode.val)
            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        result.append(currentLevel)

    return result
