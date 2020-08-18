
"""
Leetcode: 415 Add Strings

Attempts: 1
Completed: N
Acheived Ideal: N

Time Complexity: O(max(n1,n2))
Space Complexity: O(max(n1,n2))

Pattern: Array Manipulation
Technique: 

Problems Encountered: While loop needs to run up till the last digit of the longer number
Other Solutions:

"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = []

        carry = 0
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        while p1 >= 0 or p2 >= 0:
            x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            res.append(value)
            p1 -= 1
            p2 -= 1

        if carry:
            res.append(carry)

        return ''.join(str(x) for x in res[::-1])
