"""
Leetcode:91. Decode Ways

Attempts: 1
Completed: N
Acheived Ideal: N
Under 30 Mins: N

Time Complexity: O(n)
Space Complexity: O(n)

Pattern: DP
Technique: Climb Stairs pattern

Problems Encountered:
Other Solutions:

"""


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        dp = [0] * (len(s) + 1)

        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1

        for i in range(2, len(s) + 1):
            two_digit = int(s[i-2: i])
            if int(s[i-1]) > 0:
                dp[i] += dp[i-1]
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i-2]

        return dp[-1]
