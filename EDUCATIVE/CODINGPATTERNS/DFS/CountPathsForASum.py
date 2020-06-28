'''
Question: Count Paths for a Sum (medium)

Time Complexity: O(nlogn) of balanced tree O(n^2) for worse case
Space Complexity: O(n)

Pattern: DFS
Technique: Do DFS and keep track of current path. For every node, iterate through
            its path backwards to see if it adds up to the sum 

'''



class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def count_paths(root, S):
  # TODO: Write your code here
  
  return DFS(root, S, [])

def DFS(node, S, cur_path):
  if not node: 
    return 0
  
  cur_path.append(node.val)
  path_sum, path_count = 0,0
  for i in range(len(cur_path)-1, -1, -1):
    path_sum += cur_path[i]
    if path_sum == S:
      path_count += 1
  
  path_count += DFS(node.left, S, cur_path)
  path_count += DFS(node.right, S, cur_path)

  cur_path.pop()

  return path_count