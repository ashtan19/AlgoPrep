# Leetcode: 357 Valid Perfect Square

# Time Complexity: O(n), Newton Method - O(logn)
# Space Complexity: O(1)
# Solving process:
# Problems Encountered:

# Other Solutions: Newton's Method


# Linear search => Bad
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while i <= num:
            square = i*i
            if square > num:
                return False
            if square == num:
                return True
            i += 1

# Very Fast


def NewtonMethod(self, num):
    r = num
    while r*r > num:
        r = (r + num/r) // 2
    return r*r == num
