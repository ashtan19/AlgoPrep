"""
Leetcode: 304. Range Sum Query 2D - Immutable

Attempts: 1
Completed: Y
Acheived Ideal: N
Under 30 Mins: Y

Time Complexity: O(mn) for initialization O(m) for lookup where m is num rows
Space Complexity: O(mn)

Pattern: DP
Technique: 

Problems Encountered:
Other Solutions: Can acheive O(1) lookup by caching 2D cumulative 

"""


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.runningSum = [row[:] for row in matrix]
        for i in range(len(matrix)):
            curr_sum = 0
            for j in range(len(matrix[0])):
                self.runningSum[i][j] = curr_sum
                curr_sum += matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        result = 0
        rows = len(self.matrix)
        cols = len(self.matrix[0])

        for i in range(row1, row2+1):
            result += self.runningSum[i][col2] - \
                self.runningSum[i][col1] + self.matrix[i][col2]

        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
