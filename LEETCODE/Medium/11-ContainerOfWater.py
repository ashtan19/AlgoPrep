# Leetcode: 11. Container With Most Water

# Completed: N
# Acheived Ideal: N

# Time Complexity: O(n)
# Space Complexity: O(1)

# Solving process:
# Problems Encountered:

# Other Solutions:

# O(n) solution


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0
        left = 0
        right = len(height)-1

        while left < right:
            maxarea = max(maxarea, min(
                height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxarea


# Bad Solution
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxfront, frontindex, maxback, backindex = 0, 0, 0, 0
        for i in range(0, len(height)):
            front = i + height[i]
            back = len(height) - i + height[i]
            if front >= maxfront:
                maxfront = front
                frontindex = i
            if back >= maxback:
                maxback = back
                backindex = i

        return (frontindex - backindex) * min(height[backindex], height[frontindex])
