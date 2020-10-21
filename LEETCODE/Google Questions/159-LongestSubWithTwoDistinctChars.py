"""
Leetcode: 159. Longest Substring with At Most Two Distinct Characters

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Sliding Window
Technique: Track distinct Chars with hashmap

Problems Encountered: Did not check for syntax errors and edge cases
Other Solutions:

"""


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        if n <= 2:
            return n

        l = 0
        chars = {}
        result = 0

        for r in range(n):
            char_count = chars.get(s[r], 0) + 1
            chars[s[r]] = char_count
            while len(chars) > 2:
                chars[s[l]] -= 1
                if chars[s[l]] == 0:
                    del chars[s[l]]
                l += 1
            result = max(result, r-l+1)

        return result
