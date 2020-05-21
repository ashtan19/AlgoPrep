# Leetcode: 48 Rotate Image

# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Acheived Ideal: Yes Very Fast

# Solving process:
# Problems Encountered:

# Other Solutions:


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if matrix == None:
            return None
        if matrix == [[]]:
            return matrix
        rc = 0  # ringcount
        matrixlen = len(matrix[0])-1

        while rc < (matrixlen+1)//2:
            n = matrixlen - rc
            for i in range(rc, n):
                matrix[rc][i], matrix[i][n], matrix[n][matrixlen - i], matrix[matrixlen -
                                                                              i][rc] = matrix[matrixlen-i][rc], matrix[rc][i], matrix[i][n], matrix[n][matrixlen - i]

            rc += 1
