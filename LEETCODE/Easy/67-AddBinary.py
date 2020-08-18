

"""
Leetcode: 67 Add Binary

Attempts: 1
Completed: Y
Acheived Ideal: Y

Time Complexity: O(1) => if you use the bin function / O(max(a,b))
Space Complexity: O(1) => if you use the bin function / O(max(a,b))

Pattern: While Loop for addition 
Technique: 

Problems Encountered:
Other Solutions: Use built in bin function in python

"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        res = []

        p1 = len(a)-1
        p2 = len(b)-1
        carry = 0

        while p1 >= 0 or p2 >= 0:
            x1 = ord(a[p1]) - ord('0') if p1 >= 0 else 0
            x2 = ord(b[p2]) - ord('0') if p2 >= 0 else 0
            value = (x1 + x2 + carry) % 2
            carry = (x1 + x2 + carry) // 2
            res.append(value)
            p1 -= 1
            p2 -= 1

        if carry:
            res.append(carry)

        return ''.join(str(x) for x in res[::-1])


class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]


class Solution:
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]
