# Leetcode: 53 Largest SubArray (Did not finish - must try again)

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solving process: Sum it up iteratively starting from element 1. If the cur element is bigger than current sum then ditch the current sum
# Problems Encountered: Thought Process was difficult

# Other Solutions: Divide and conquer


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        curSum = maxSum = nums[0]

        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum
