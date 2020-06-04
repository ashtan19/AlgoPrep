# Leetcode: 53 Largest SubArray (Did not finish - must try again)

# Attempts: 2
# Completed: Y
# Ideal: Y

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solving process: Sum it up iteratively starting from element 1. If the cur element is bigger than current sum then ditch the current sum
# Problems Encountered: Thought Process was difficult

# Other Solutions: Divide and conquer

# Attempt 2. Passed


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or nums == []:
            return None
        maxsum, currsum = nums[0], nums[0]

        for i in range(1, len(nums)):
            currsum += nums[i]
            if currsum < nums[i]:
                currsum = nums[i]
            if currsum > maxsum:
                maxsum = currsum
        return maxsum


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
