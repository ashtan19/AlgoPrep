"""
Leetcode: 55 Jump Game

Attempts: 1
Completed: Y
Acheived Ideal: Y ? => There is a traditional DP solution that will be slower and take more space but it may be the solution 
                the interviewer wants

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: DP
Technique: Suffix Problem => Start from the back and keep track of the min distance that you would need to array to hold true

Problems Encountered: Did not think of the edge cases
Other Solutions:

"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        minDistance = 0
        canMakeIt = False
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > minDistance:
                minDistance = 0
                canMakeIt = True
            else:
                minDistance += 1
                canMakeIt = False

        return canMakeIt
