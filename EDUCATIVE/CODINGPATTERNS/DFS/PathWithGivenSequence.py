'''
Question: Path With Given Sequence

Time Complexity: O(n)
Space Complexity: O(n)

Pattern: DFS
Technique: 


'''


def find_path(root, sequence):
    # TODO: Write your code here

    return DFS(root, sequence, 0)


def DFS(root, sequence, index):
    if root and index < len(sequence) and root.val == sequence[index]:
        if root.left == None and root.right == None:
            return True

        return DFS(root.left, sequence, index+1) or DFS(root.right, sequence, index + 1)
    return False
