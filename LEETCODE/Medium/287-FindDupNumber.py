# Leetcode: 287 Find the Duplicate Number

# Completed: Y
# Acheived Ideal: N

# Time Complexity:  O(n) O(n)
# Space Complexity: O(n) O(1)

# Solving process:
# Problems Encountered:

# Other Solutions: Floyd's Tortoise and Hare Cycle Detection


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsDict = {}
        for num in nums:
            if num in numsDict:
                return num
            else:
                numsDict[num] = 1

        return None


# Floyd's Tortoise and Hare Cycle Detection
class Solution:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare
