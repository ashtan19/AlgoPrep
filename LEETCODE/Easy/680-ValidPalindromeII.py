"""
Leetcode: 680. Valid Palindrome II

Attempts: 2
Completed: Y but not first try
Acheived Ideal: Y but can optimize for less space
Under 30 Mins: Y

Time Complexity: O(n)
Space Complexity: O(n)

Pattern: Two Pointer
Technique: 

Problems Encountered: Needed some reminder on how to effectively solve palindromes
Other Solutions: Can also iterate in isPalindrome to save space

"""


class Solution(object):
    def validPalindrome(self, s):
        if s == s[::-1]:
            return True

        def isPalindrome(s):
            if s == s[::-1]:
                return True
            else:
                return False
        p1, p2 = 0, len(s)-1

        while p1 < p2:
            if s[p1] != s[p2]:
                break
            p1 += 1
            p2 -= 1

        if p1 >= p2:
            return True
        else:
            return isPalindrome(s[p1+1:p2+1]) or isPalindrome(s[p1:p2])
