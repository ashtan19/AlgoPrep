# Leetcode: 198 House Robber

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

# Memoization


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.memo = [-1]*len(nums)
        return self.robHelper(nums, len(nums)-1)

    def robHelper(self, nums, i):
        if (i < 0):
            return 0
        if self.memo[i] >= 0:
            return self.memo[i]
        result = max(self.robHelper(nums, i-2) +
                     nums[i], self.robHelper(nums, i-1))
        self.memo[i] = result
        return result

#Iterative + memo


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        memo = [-1]*(len(nums)+1)
        memo[0] = 0
        memo[1] = nums[0]

        for i in range(1, len(nums)):
            val = nums[i]
            memo[i+1] = max(memo[i], memo[i-1]+val)
        return memo[len(nums)]
