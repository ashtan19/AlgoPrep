# Leetcode: 1 Two Sum

# Time Complexity: O(n^2), O(n)
# Space Complexity: O(1), O(n)
# Solving process:
# Problems Encountered:

# Other Solutions:

# Iterative Brute Force


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# HashMap


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i
