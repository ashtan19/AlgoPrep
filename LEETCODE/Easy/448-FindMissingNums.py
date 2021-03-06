# Leetcode: 448 Find Dissapeared Numbers

# Attempts: 2

# Time Complexity: O(n)
# Space Complexity: O(n) O(1)
# Solving process:
# Problems Encountered:

# Other Solutions: Mark the numbers with -1, then run through array again to find indexes that are not negated

import collections


class Solution:
    def findDisappearedNumbers(self, nums):
        hashmap = collections.Counter(nums)
        retarr = []
        for i in range(0, len(nums)):
            if not hashmap[i+1]:
                retarr.append(i+1)
            print(i)
        return retarr


testSolution = Solution()
print(testSolution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))


# Second Solution

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] *= -1

        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)

        return res

# Attempt 2


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            pointer = abs(nums[i])-1
            if nums[pointer] > 0:
                nums[pointer] *= -1
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
        return result
