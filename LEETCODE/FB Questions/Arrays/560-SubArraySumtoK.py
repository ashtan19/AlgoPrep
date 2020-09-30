"""
Leetcode: 560. Subarray Sum Equals K

Attempts: 1
Completed: Y 
Acheived Ideal: Y 
Under 30 Mins: N

Time Complexity: O(n)
Space Complexity: O(n)

Pattern: Array Traversal with Summation
Technique: Keep track of a contiguous sum and also the number of times that the contiguous sum occurred. Find result by finding curr_sum-k in hashtable

Problems Encountered:
Other Solutions:

"""


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        sum_map = {0: 1}
        result = 0
        curr_sum = 0

        for i in range(0, len(nums)):
            curr_sum += nums[i]
            result += sum_map.get(curr_sum-k, 0)
            sum_map[curr_sum] = sum_map.get(curr_sum, 0) + 1

        return result
