"""
Leetcode: 283 Move Zeroes

Attempts: 1
Completed: Y 
Acheived Ideal: Y 
Under 30 Mins: 

Time Complexity:
Space Complexity:

Pattern: 
Technique: 

Problems Encountered:
Other Solutions:

"""

'''
1) have a pointer that points to the next available index for a valid number
2) Iterate over array and if number is not zero, switch numbers or set valid number and then set to zero 
'''


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        next_aval = 0

        for i in range(0, len(nums)):
            if nums[i] != 0:
                if i == next_aval:
                    next_aval += 1
                    continue
                nums[next_aval] = nums[i]
                next_aval += 1
                nums[i] = 0
