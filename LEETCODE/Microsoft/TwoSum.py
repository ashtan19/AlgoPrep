"""
Leetcode: 1. Two Sum

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(n)
Space Complexity: O(n)

Pattern: Array
Technique: Use hashtable to track past nums for compliment

Problems Encountered:
Other Solutions:

"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        table = {nums[0]: 0}
        n = len(nums)

        for i in range(1, n):
            cur = nums[i]
            comp = target - cur
            if comp in table:
                return [i, table[comp]]
            table[cur] = i
