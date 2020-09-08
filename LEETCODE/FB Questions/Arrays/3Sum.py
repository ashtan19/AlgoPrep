'''
Question: 3 Sum

Time Complexity: O(n^2)
Space Complexity: O(n) ignoring the result array 

Pattern: Two Pointer 
Technique: Two Pointer method N times. Checking for duplicates and skipping them

'''

'''
Two Pointer 
Algorithm:
1) Sort the Array of numbers
2) iterate over the array from front to back
3) Skip over the duplicate numbers
4) have a while loop checks for a target sum by having a left and right pointer 
5) pointer will skip on the duplicate numbers 

'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []

        def searchPairs(nums, targetSum, left, result):
            right = len(nums) - 1
            while left < right:
                currentSum = nums[left] + nums[right]
                if currentSum == targetSum:
                    result.append([-targetSum, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < len(nums) and nums[left] == nums[left-1]:
                        left += 1
                    while right >= 0 and nums[right] == nums[right + 1]:
                        right -= 1
                elif currentSum < targetSum:
                    left += 1
                else:
                    right -= 1

        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            searchPairs(nums, -nums[i], i+1, result)

        return result
