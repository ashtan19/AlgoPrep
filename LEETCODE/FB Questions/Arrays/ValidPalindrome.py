"""
Leetcode: 125. Valid Palindrome

Attempts: 1
Completed: Y 
Acheived Ideal: Y 
Under 30 Mins: Y

Time Complexity: O(n)
Space Complexity: O(n)

Pattern: String Manipulation
Technique: 

Problems Encountered:
Other Solutions: Can use two pointer technique to move outside to inside

"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lowered_s = s.lower()
        filtered_s = []

        for char in lowered_s:
            if char.isalnum():  # if ord(char) <= (ord("9") and ord(char) >= ord("0")) or (ord(char) >= ord("a") and ord(char) <= ord("z"))
                filtered_s.append(char)

        reversed_s = "".join(filtered_s[::-1])
        filtered_s = "".join(filtered_s)
        print(filtered_s)
        if reversed_s == filtered_s:
            return True
        else:
            return False


class Solution:
    def isPalindrome(self, s: str) -> bool:

        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if i < j and s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True
