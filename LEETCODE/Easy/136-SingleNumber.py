# Leetcode: 136 Single Number in Array

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solving process:
# Problems Encountered:

# Other Solutions: Use Hash Table -> but extra mem , use Math or Bit Wise


class Solution:
    def singleNumber(self, nums):
        nums.sort()
        i = 0
        while i < len(nums)-1:
            if nums[i] != nums[i+1]:
                return nums[i]
            i += 2
        return nums.pop()


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a


testSol = Solution()
testArray = [4, 1, 2, 1, 2]
print(testSol.singleNumber(testArray))
