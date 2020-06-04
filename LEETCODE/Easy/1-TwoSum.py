# Leetcode: 1 Two Sum

# Attempts: 2


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

# Attempt 2 with Hashmap


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashtable:
                return [i, hashtable[complement]]
            hashtable[num] = i
