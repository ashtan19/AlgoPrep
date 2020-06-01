# Leetcode: 283 Move Zeros

# Attempts: 2

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solving process:
# Problems Encountered:

# Other Solutions:


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        startOfZeros = 0
        runner = 0
        # Get to start of zeros
        while (runner < len(nums) and nums[runner] != 0):
            runner += 1

        startOfZeros = runner
        runner += 1

        while (runner <= len(nums)-1):
            if nums[runner] != 0:  # swap
                nums[startOfZeros] = nums[runner]
                nums[runner] = 0
                startOfZeros += 1
            runner += 1

# Attempt 2: Did not complete.


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lastNonZero = -1
        for i in range(len(nums)):
            if nums[i] != 0:
                lastNonZero += 1
                nums[lastNonZero], nums[i] = nums[i], nums[lastNonZero]
