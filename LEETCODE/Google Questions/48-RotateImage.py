"""
Leetcode: 48. Rotate Image

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(n^2)
Space Complexity: O(1)

Pattern: Matrix
Technique: Transpose and reverse

Problems Encountered:
Other Solutions: Can do in one pass instead of two. see below

"""


# Transpose and Reverse
# Potential Problems: Will not be able to transpose if matrix is not n x n
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        def transpose(matrix):
            for i in range(len(matrix)):
                for j in range(i, len(matrix[0])):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        def reflection(matrix):
            for row in range(len(matrix)):
                l, r = 0, len(matrix[row])-1
                while l < r:
                    matrix[row][l], matrix[row][r] = matrix[row][r], matrix[row][l]
                    l += 1
                    r -= 1

        transpose(matrix)
        reflection(matrix)
        return


# This solution is one pass
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp
