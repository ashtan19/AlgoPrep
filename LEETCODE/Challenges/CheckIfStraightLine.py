# Leetcode: 1232 Check if its a Straight line

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solving process:
# Problems Encountered: Division by zero

# Other Solutions: Use Multiplication Approach to check


# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

# Example 1:

# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true
# Example 2:

# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        xhashmap = {}  # Is-visited map
        if len(coordinates) <= 1:
            return False
        xhashmap[coordinates[0][0]] = coordinates[0][1]
        if coordinates[1][0] in xhashmap:
            return False
        xhashmap[coordinates[1][0]] = coordinates[1][1]

        slope = (coordinates[1][1] - coordinates[0][1]) / \
            (coordinates[1][0] - coordinates[0][0])
        intercept = coordinates[0][1] - slope*(coordinates[0][0])

        for i in range(2, len(coordinates)-1):
            if (coordinates[i][0] in xhashmap or coordinates[i][1] != (slope*(coordinates[i][0]) + intercept)):
                return False
            xhashmap[coordinates[i][0]] = coordinates[i][1]

        return True


def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    (x0, y0), (x1, y1) = coordinates[: 2]
    for x, y in coordinates:
        if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
            return False
    return True


def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    (x0, y0), (x1, y1) = coordinates[: 2]
    return all((x1 - x0) * (y - y1) == (x - x1) * (y1 - y0) for x, y in coordinates)
