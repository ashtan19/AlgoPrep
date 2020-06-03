# Leetcode: 1029. Two City Scheduling

# Attempts: 1
# Completed: N
# Acheived Ideal:

# Time Complexity: O(nlogn)
# Space Complexity: O(n)

# Solving process: Find the cost if all went to first city. Then sort the differences and send half with min
#                   difference to second city
# Problems Encountered:

# Other Solutions:


class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        firstCity = [i for i, j in costs]
        difference = [j-i for i, j in costs]

        difference.sort()

        return sum(firstCity) + sum(difference[:len(difference)/2])
