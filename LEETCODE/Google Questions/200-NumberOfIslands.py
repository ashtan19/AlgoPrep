"""
Leetcode: 200. Number of Islands

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(m*n)
Space Complexity: O(m*n)

Pattern: Matrix 
Technique: BFS search for points with "1". Mark the points that are reachable from current point 

Problems Encountered:
Other Solutions: Union Find

"""


'''
Idea: 
- Iterate through the whole matrix
- When you encounter a 1, add it's neighbours to a queue if they are 1's 
- Flip the 1 to a # 
- Go through the queue to mark all the 1's that are connected 
- increment result by 1

'''


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        from collections import deque

        rows = len(grid)
        cols = len(grid[0])

        def find_island(queue, grid):
            while queue:
                x, y = queue.popleft()
                if y > 0 and grid[x][y-1] == "1":
                    grid[x][y-1] = "#"
                    queue.append((x, y-1))
                if y < len(grid[0])-1 and grid[x][y+1] == "1":
                    grid[x][y+1] = "#"
                    queue.append((x, y+1))
                if x > 0 and grid[x-1][y] == "1":
                    grid[x-1][y] = "#"
                    queue.append((x-1, y))
                if x < len(grid)-1 and grid[x+1][y] == "1":
                    grid[x+1][y] = "#"
                    queue.append((x+1, y))

        result = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    queue = deque([(i, j)])
                    grid[i][j] = "#"
                    find_island(queue, grid)
                    result += 1

        return result
