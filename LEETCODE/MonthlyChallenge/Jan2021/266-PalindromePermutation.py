"""
Leetcode:266. Palindrome Permutation

Attempts:1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Palindrome
Technique: Use hashtable

Problems Encountered:
Other Solutions: Can also use set. If set has more than 1 left, return false

"""


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        from collections import Counter

        chars = Counter(s)
        odd_count = 0

        for value in chars.values():
            if value % 2 == 1:
                odd_count += 1

            if odd_count > 1:
                return False

        return True
