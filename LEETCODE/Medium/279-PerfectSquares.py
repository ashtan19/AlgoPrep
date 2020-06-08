# Leetcode: 279. Perfect Squares

# Attempts: 1
# Completed: Y
# Acheived Ideal: N

# Time Complexity: n^2
# Space Complexity:

# Solving process:
# Problems Encountered:

# Other Solutions: Static DP


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.mapping = {0: 0, 1: 1}
        self.squares = []
        i = 0
        while i*i < n:
            self.squares.append(i*i)
            i += 1
        self.squares.append(i*i)

        currsquare = 1
        for j in range(2, n+1):
            if j not in self.mapping:
                min = float("inf")
                if self.squares[currsquare+1] <= j:
                    currsquare += 1
                for squareindex in range(1, currsquare+1):
                    compliment = j - self.squares[squareindex]
                    numcomp = self.mapping[compliment]
                    if min > numcomp:
                        min = numcomp
                self.mapping[j] = min + 1
        return self.mapping[n]

# Static DP


class Solution(object):
    _dp = [0]

    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]
