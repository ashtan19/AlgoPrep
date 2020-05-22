# Leetcode: 38 Combination Sum
# Completed: No

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# Acheived Ideal:

# Solving process: Do a DFS on every element. Set index to current element b/c we know that previous elements dont work
# Problems Encountered:

# Other Solutions: Can also use backtracking, Dynamic programming


# DFS Solution
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = []
        candidates.sort()
        self.dfs(candidates, 0, target, [], result)
        return result

    def dfs(self, nums, index, target, path, result):
        if target == 0:
            result.append(path)
            return
        for i in range(index, len(nums)):
            if nums[i] > target:
                break
            else:
                self.dfs(nums, i, target - nums[i], path + [nums[i]], result)
