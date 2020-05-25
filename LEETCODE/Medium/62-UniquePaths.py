# Leetcode: 62. Unique Paths

# Completed: N
# Acheived Ideal: N

# Time Complexity:
# Space Complexity: O(n)

# Solving process:
# Problems Encountered:

# Other Solutions:


# Dynamic Programming O(m*n) space
def uniquePaths2(self, m, n):
    if not m or not n:
        return 0
    dp = [[1 for _ in xrange(n)] for _ in xrange(m)]
    for i in xrange(1, m):
        for j in xrange(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]

# O(n) space


def uniquePaths(self, m, n):
    if not m or not n:
        return 0
    cur = [1] * n
    for i in xrange(1, m):
        for j in xrange(1, n):
            cur[j] += cur[j-1]
    return cur[-1]
