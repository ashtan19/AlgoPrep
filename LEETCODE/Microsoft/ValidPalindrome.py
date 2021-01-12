"""
Leetcode: 125. Valid Palindrome

Attempts: 1
Completed: Y
Acheived Ideal: N
Under 30 Mins: Y

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: String Manipulation
Technique: Clean the str and compare reverse

Problems Encountered:
Other Solutions: Use two pointer

"""

# Two Pointer solution O(n), O(1 space)


class Solution:
    def isPalindrome(self, s: str) -> bool:

        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        clean_str = []
        s = s.lower()
        n = len(s)

        for c in s:
            if c.isalnum():
                clean_str.append(c)

        clean_str = "".join(clean_str)
        print(clean_str)
        return clean_str == clean_str[::-1]
