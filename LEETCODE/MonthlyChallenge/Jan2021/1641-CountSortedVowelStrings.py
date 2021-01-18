"""
Leetcode:1641. Count Sorted Vowel Strings

Attempts: 1
Completed: Y
Acheived Ideal: Yes
Under 30 Mins: N0

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Combinatorics
Technique: FInd the patterns in the vowel strings

Problems Encountered:
Other Solutions: There is a cleaner math solution, Can also use DP

"""


class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math

        memo = {}

        def nCr(n, r, memo):
            if (n, r) in memo:
                return memo[(n, r)]

            f = math.factorial
            memo[(n, r)] = f(n) / f(r) / f(n-r)
            return memo[(n, r)]

        result = 0

        if n > 0:
            result += 5
        if n-1 > 0:
            result += (n-1) * 10
        if n-2 > 0:
            result += nCr(n-1, 2, memo) * 10
        if n-3 > 0:
            result += nCr(n-1, 3, memo) * 5
        if n-4 > 0:
            result += nCr(n-1, 4, memo)

        return result


# Cleaner math Solution
class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (n+4) * (n+3) * (n+2) * (n+1) / 24
