"""
Leetcode: 139. Word Break

Attempts: 1
Completed: N
Acheived Ideal: n
Under 30 Mins: N

Time Complexity: O(n^3)
Space Complexity: O(n)

Pattern: DP
Technique: Use a 1D DP table to keep track of which sequences prior to a matched word is also valid

Problems Encountered: Didnt have the intuition to iterate through the list of words
Other Solutions: 

"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)

        dp[0] = True

        for i in range(len(s)):
            for w in wordDict:
                if i >= len(w)-1 and s[i-len(w)+1: i+1] == w and dp[i-len(w)+1]:
                    dp[i+1] = True
                    break
                else:
                    dp[i+1] = False
        print(dp)
        return dp[-1]
