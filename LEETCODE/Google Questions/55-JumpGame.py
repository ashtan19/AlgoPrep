"""
Leetcode: 55. Jump Game

Attempts: 1
Completed: N
Acheived Ideal: N
Under 30 Mins: N

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: DP or Array Manipulation 
Technique: Keep Track of how far you can get (you are searching through your current can_reach)
            return false when you cannot expand your can_reach any further

Problems Encountered:
Other Solutions:

"""

# Cleanest way to return a boolean


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True

        n = len(nums)-1
        can_reach = 0
        i = 0

        while i <= can_reach:
            if i == n:
                return True
            can_reach = max(can_reach, i + nums[i])
            i += 1
        return False


# Can Easily change this to find the min number of jumps
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True

        curr_index = 0
        max_distance = 0
        n = len(nums)-1

        while True:
            can_reach = -1
            for i in range(curr_index, max_distance+1):
                can_reach = max(i + nums[i], can_reach)

            if can_reach >= n:
                return True
            curr_index = max_distance + 1
            max_distance = can_reach

            if curr_index > max_distance:
                return False
