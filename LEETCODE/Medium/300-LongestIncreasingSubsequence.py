# Leetcode: 300. Longest Increasing Subsequence

# Attempts: 1
# Completed: N
# Acheived Ideal: N

# Time Complexity:
# Space Complexity:

# Solving process:
# Problems Encountered:

# Other Solutions: Can also do binary search


# Memo and recursion O(n^2) O(n^2)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = [[-1]*len(nums) for i in range(len(nums)+1)]

        def find_length(nums, prev, position):
            if position == len(nums):
                return 0
            if memo[prev+1][position] >= 0:
                return memo[prev+1][position]
            taken = 0
            if prev < 0 or nums[position] > nums[prev]:
                taken = 1 + find_length(nums, position, position + 1)
            nottaken = find_length(nums, prev, position+1)
            memo[prev+1][position] = max(taken, nottaken)
            return memo[prev+1][position]

        return find_length(nums, -1, 0)

# DP (Prefix)
# How it works: keep track of a list of longest subsequences
# when adding a new element at the end, check all previous elements if bigger
# if current element is bigger, add 1 to the longest subsequence
# Keep track of longest subsequence that you can add to


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or nums == []:
            return 0
        dp = [1]
        maxans = 1
        for i in range(1, len(nums)):
            maxval = 0
            for j in range(0, i):
                if nums[i] > nums[j]:
                    maxval = max(maxval, dp[j])
            dp.append(maxval + 1)
            maxans = max(maxans, dp[i])
        return maxans

# Binary Search - Tough


def lengthOfLIS(self, nums):
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) / 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size
