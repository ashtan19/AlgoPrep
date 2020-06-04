# Leetcode: 200. Number of Islands

# Attempts:1
# Completed:1
# Acheived Ideal:Y

# Time Complexity: O(4n*m)
# Space Complexity: O(n*m)

# Solving process:
# Problems Encountered:

# Other Solutions: Instead of creating a hashtable, you could also change the value of a seen plot
#                   other than 0 or 1

# Attempt 1: recursion and memoization. Passed


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        self.plotseen = {}
        icounter = 0
        if grid == [[]] or grid == [] or grid == None:
            return 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in self.plotseen:

                    self.markseen(row, col, grid)
                    icounter += 1

        return icounter

    def markseen(self, row, col, grid):
        if grid[row][col] == "1" and (row, col) not in self.plotseen:
            self.plotseen[row, col] = True
            if row + 1 < len(grid):
                self.markseen(row+1, col, grid)
            if col+1 < len(grid[0]):
                self.markseen(row, col+1, grid)
            if row - 1 >= 0:
                self.markseen(row-1, col, grid)
            if col - 1 >= 0:
                self.markseen(row, col-1, grid)
