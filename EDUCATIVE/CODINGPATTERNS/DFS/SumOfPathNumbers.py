'''
Question: Sum of Path Numbers

Time Complexity: O(n)
Space Complexity: O(n)

Pattern: DFS
Technique: 


'''


def find_sum_of_path_numbers(root):
    # TODO: Write your code here

    return DFS(root, 0)


def DFS(root, current_digits):
    if root is None:
        return 0
    current_digits = (current_digits * 10) + root.val
    if root.left == None and root.right == None:
        return current_digits
    return DFS(root.left, current_digits) + DFS(root.right, current_digits)
