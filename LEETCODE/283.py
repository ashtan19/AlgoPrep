# Leetcode: 283 Move Zeros

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solving process:
# Problems Encountered: 

# Other Solutions:


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        startOfZeros = 0
        runner = 0
        while (runner < len(nums) and nums[runner] != 0): #Get to start of zeros
            runner += 1
            
        startOfZeros = runner
        runner += 1
        
        while (runner <= len(nums)-1):
            if nums[runner] != 0: #swap
                nums[startOfZeros] = nums[runner]
                nums[runner] = 0 
                startOfZeros += 1
            runner += 1