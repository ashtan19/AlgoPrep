# Leetcode: 581 Shortest Unsorted Continuous Subarray

# Time Complexity: O(nlogn)
# Space Complexity: O(n)
# Solving process:
# Problems Encountered:

# Other Solutions: Can use a stack although complicated - must try again


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = stop = None
        copy = nums[:]
        copy.sort()

        for i in range(0, len(nums)):
            if copy[i] != nums[i]:
                if start == None:
                    start = stop = i
                else:
                    stop = i

        if start == None:
            return 0
        else:
            return stop - start + 1
