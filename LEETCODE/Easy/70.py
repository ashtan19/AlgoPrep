# Leetcode: 70 Climbing Stairs

# Time Complexity: O(n) - memoization
# Space Complexity: O(n) - memo
# Solving process:
# Problems Encountered:

# Other Solutions: Use Dynamic Programming or Fibonacci


class Solution(object):
    memo = {}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            if n-1 not in self.memo:
                self.memo[n-1] = self.climbStairs(n-1)
            if n-2 not in self.memo:
                self.memo[n-2] = self.climbStairs(n-2)
            return self.memo[n-1] + self.memo[n-2]


def climbStairs(self, n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a
