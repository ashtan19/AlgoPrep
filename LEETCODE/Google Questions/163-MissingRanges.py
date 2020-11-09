"""
Leetcode: 163 Missing Ranges 

Attempts:1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(n)
Space Complexity: O(n)

Pattern: Iteration
Technique: Iterate through the nums array to find the missing ranges 

Problems Encountered:
Other Solutions: Can add the upper bound to the nums array to skip the last check

"""


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]

        nums = [0,1,3,50,75], lower = 0, upper = 99
        """

        n = len(nums)
        l = lower
        result = []

        for i in range(n):
            num = nums[i]
            if l < num:
                if num-1 == l:
                    result.append(str(l))
                else:
                    result.append(str(l) + "->" + str(num-1))
            l = num + 1

        if l <= upper:
            if l == upper:
                result.append(str(l))
            else:
                result.append(str(l) + "->" + str(upper))

        return result
