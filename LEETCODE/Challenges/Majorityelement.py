# Leetcode: May Challenge Majority Element

# Time Complexity: O(nlogn)
# Space Complexity: O(1)
# Solving process:
# Problems Encountered: 

# Other Solutions:

# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3
# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        half = int(len(nums)/2)
        if len(nums) % 2 == 1:
            if nums[0] == nums[half]:
                return nums[0]
            else: return nums[half]
        else: 
            if nums[0] == nums[half - 1]:
                return nums[0]
            else: return nums[half]