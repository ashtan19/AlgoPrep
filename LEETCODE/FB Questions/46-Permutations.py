"""
Leetcode: 46. Permutations

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(N * N!)
Space Complexity: O(N!)

Pattern: Recursion
Technique: Backtracking

Problems Encountered: Remember that you have to create a new copy of nums when you append
Other Solutions: 

"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == None or nums == []:
            return [nums]
        result = []

        def backtrack(nums, result, start):
            if start == len(nums)-1:
                result.append(nums[:])
                return
            backtrack(nums, result, start+1)
            for i in range(start+1, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(nums, result, start+1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(nums, result, 0)
        return result
