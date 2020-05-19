# Leetcode: 46 Get Permutations

# Time Complexity: O(n*n!)
# Space Complexity: O(n*n!)
# Solving process: Use Backtracking to find all permutations
# Problems Encountered:

# Other Solutions: Use the built in permutation tool - Not really a solution


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.backtracking(nums, 0, len(nums)-1)
        return self.result

    def backtracking(self, nums, first, last):

        if first == last:
            self.result.append(nums)
        else:
            for i in range(first, last+1):
                nums[first], nums[i] = nums[i], nums[first]
                self.backtracking(nums[:], first+1, last)
                nums[first], nums[i] = nums[i], nums[first]
