"""
Leetcode: 489. Robot Room Cleaner

Attempts: 1
Completed: N 
Acheived Ideal: N
Under 30 Mins: N

Time Complexity: O(n-m)
Space Complexity: O(n-m) b/c of visited set

Pattern: Graph
Technique: Recursive Spiral Backtracking 

Problems Encountered: Knew that it needed some backtracking but did not know how to implement
Other Solutions:

"""


# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

'''
Idea: 
DFS search on room 
Need a stack to keep track of the path it has taken 
Need a queue to keep track of the possible tiles that it can go 
Have a stack with a queue as an entry 
Have a visited set to keep track of the tiles that have been cleaned
'''


class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(cell=(0, 0), d=0):
            visited.add(cell)
            robot.clean()

            for i in range(4):
                new_d = (d + i) % 4
                new_cell = (cell[0] + directions[new_d][0],
                            cell[1] + directions[new_d][1])
                if new_cell not in visited and robot.move():
                    backtrack(new_cell, new_d)
                    go_back()

                robot.turnRight()

        backtrack()
