"""
Leetcode: 680. Valid Palindrome II

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(n)
Space Complexity: O(n)

Pattern: Array Traversal
Technique: 

Problems Encountered:
Other Solutions:

"""


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def isPalindrome(s):
            r = s[::-1]
            if r == s:
                return True
            else:
                return False

        l, r = 0, len(s)-1

        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if isPalindrome(s[l+1: r+1]):
                    return True
                elif isPalindrome(s[l: r]):
                    return True
                else:
                    return False

        return True
