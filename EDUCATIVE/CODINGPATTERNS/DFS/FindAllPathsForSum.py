'''
Question: All Paths for a Sum (medium)

Time Complexity: O(n)
Space Complexity: O(n)

Pattern: DFS
Technique: 


'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    allPaths = []
    # TODO: Write your code here
    if not root:
        return
    cur_path = []
    DFS(root, allPaths, cur_path, sum)

    return allPaths


def DFS(root, allPaths, cur_path, sum):
    if not root:
        return
    cur_sum = sum - root.val
    cur_path.append(root.val)
    if sum == root.val:
        allPaths.append(list(cur_path))
    if root.left:
        DFS(root.left, allPaths, cur_path, cur_sum)
    if root.right:
        DFS(root.right, allPaths, cur_path, cur_sum)
    cur_path.pop()
    return
