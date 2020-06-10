# Leetcode: 416. Partition Equal Subset Sum

# Attempts: 1
# Completed: N
# Acheived Ideal: N

# Time Complexity: O(n^2)
# Space Complexity:

# Solving process: 0/1 Knapsack with boolean matrix
# Problems Encountered: Very tough to conceptualize

# Other Solutions:



class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cursum = sum(nums)
        if cursum % 2 == 1:
            return False

        cursum /= 2

        n = len(nums)
        dp = [[False]*(cursum+1) for i in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True

        for i in range(1, n+1):
            for j in range(1, (cursum+1)):
                dp[i][j] = dp[i-1][j]
                if (j >= nums[i-1]):
                    dp[i][j] = dp[i][j] or dp[i-1][j-nums[i-1]]
        return dp[n][cursum]
