# Leetcode: 64 Minimum Path Sum

# Completed: Y
# Acheived Ideal: N

# Time Complexity: O(2^(n*m))
# Space Complexity: Massive

# Solving process:
# Problems Encountered:

# Other Solutions: Use Dynamic Programming



# Brute Force and Explore all options
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == None or grid == []:
            return None
        # If grid is a 1D array
        # if isInstance(grid[0], list) is False:
        #     return sum(grid)
        if grid == [[]]:
            return None
        self.n = len(grid) - 1
        self.m = len(grid[0]) - 1
        self.min = float('inf')

        self.nextStep(grid, 0, 0, 0)

        return self.min

    def nextStep(self, grid, currN, currM, currSum):
        currSum += grid[currN][currM]
        if currN == self.n and currM == self.m:
            if currSum < self.min:
                self.min = currSum
            return
        if currM < self.m:
            self.nextStep(grid, currN, currM+1, currSum)
        if currN < self.n:
            self.nextStep(grid, currN+1, currM, currSum)


# Dynamic Programming Solution
def minPathSum(self, grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(1, n):
        grid[0][i] += grid[0][i-1]
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]
