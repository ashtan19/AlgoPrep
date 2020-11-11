"""
Leetcode: 42 Trapping Rain water

Attempts: 1
Completed: N
Acheived Ideal: N
Under 30 Mins: N

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Array min max 
Technique: Can calculate the volume of water for an index by taking the min of left_max and right_max of the index and 
            subtract the current value at index. 
            This is a min max problem and can be solved with a two pointer approach to find the lower envelope

Problems Encountered:
Other Solutions: DP or Lower Envelop 

"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n < 3:
            return 0

        l, r = 0, n-1
        l_max, r_max = 0, 0
        total_water = 0

        while l < r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
            if l_max <= r_max:
                total_water += l_max - height[l]
                l += 1
            else:
                total_water += r_max - height[r]
                r -= 1

        return total_water
