# Leetcode: 198 House Robber - Try Again

# Attempts: 2

# Time Complexity: O(2^n) , O(n) , O(n)
# Space Complexity: O(n), O(n), O(1)
# Solving process:
# Problems Encountered:

# Other Solutions: Plain Recursion, Rec + Memo, Iterative + memo

# Plain Recursion


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.robHelper(nums, len(nums)-1)

    def robHelper(self, nums, i):
        if (i < 0):
            return 0
        return max(self.robHelper(nums, i-2)+nums[i], self.robHelper(nums, i-1))

# DP


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or nums == []:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        memo = [None] * (len(nums)+1)
        memo[0] = 0
        memo[1] = nums[0]
        i = 1
        while i < len(nums):
            memo[i+1] = max(memo[i-1]+nums[i], memo[i])
            i += 1
        return memo[len(nums)]

# Static DP


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or nums == []:
            return 0
        prev1 = 0
        prev2 = 0
        for num in nums:
            tmp = prev1
            prev1 = max(prev1, prev2+num)
            prev2 = tmp
        return prev1
