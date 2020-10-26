"""
Leetcode: 1328. Break a Palindrome

Attempts: 1
Completed: Y but missed many edge cases 
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(n)
Space Complexity: O(n) b/c of constructing the return string

Pattern: Array Manipulation 
Technique: 

Problems Encountered: Missed many edge cases of the for loop when n <= 4
Other Solutions:

"""


class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        n = len(palindrome)
        if n == 1:
            return ""

        halfway = n // 2 - 1
        if n <= 4:
            halfway += 1

        for i in range(halfway):
            if palindrome[i] != "a":
                return palindrome[:i] + "a" + palindrome[i+1:]

        return palindrome[:n-1] + "b"


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ''
        for i, char in enumerate(palindrome):
            if char != 'a' and i != n//2:
                return palindrome[:i] + 'a' + palindrome[i+1:]
            elif char == 'a' and i == n - 1:
                return palindrome[:-1] + 'b'
