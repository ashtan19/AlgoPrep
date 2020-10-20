"""
Leetcode: 11. Container With Most Water

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Sliding Window 
Technique: Decrease window on the left side if left height is smaller else opposite

Problems Encountered:
Other Solutions:

"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n <= 1:
            return 0
        max_area = 0
        l, r = 0, n-1

        while l < r:
            curr_area = min(height[l], height[r]) * (r-l)
            max_area = max(max_area, curr_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
