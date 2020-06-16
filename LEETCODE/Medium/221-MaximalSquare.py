# Leetcode: 221. Maximal Square

# Attempts: 1
# Completed: Y
# Acheived Ideal: N

# Time Complexity: O(n^4)
# Space Complexity: O(n^2)

# Solving process:
# Problems Encountered:

# Other Solutions:


'''
Input: Given a matrix of 0s and 1s
Output: the largest square area of 1s

Sample: 
Input:      Output: 4

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Need to have visited matrix

Need a helper function: give it an point in the matrix 
0) set to visited
1) check if current point is 1 -> if no, return 0
2) check if right, down and diagonal i 1 -> if not, or if outof bounds, return 1
3) if all four points are 1, then call function on all four
4) take min(all 3 adjacent points) + 1 and set current point 
5) return current point value 
'''

# Super Slow


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if matrix == [] or matrix == None:
            return 0
        visitedMatrix = [row[:] for row in matrix]
        maxArea = 0
        numRows = len(matrix)
        numCols = len(matrix[0])

        def getDimensions(row, col):
            if int(visitedMatrix[row][col]) > 1:
                return visitedMatrix[row][col]
            if matrix[row][col] == "0":
                return 0
            # Check bounds
            if row+1 >= numRows or col+1 >= numCols:
                return 1
            right = getDimensions(row, col+1)
            bottom = getDimensions(row+1, col)
            diagonal = getDimensions(row+1, col+1)
            visitedMatrix[row][col] = (min(right, bottom, diagonal) + 1)
            return visitedMatrix[row][col]

        for i in range(0, numRows):
            for j in range(0, numCols):
                if visitedMatrix[i][j] != '0':
                    dimension = getDimensions(i, j)
                    maxArea = max(maxArea, dimension**2)

        return maxArea


# DP Solution
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None or len(matrix) < 1:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0]*(cols+1) for _ in range(rows+1)]
        max_side = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    # Be careful of the indexing since dp grid has additional row and column
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1
                    max_side = max(max_side, dp[r+1][c+1])

        return max_side * max_side
