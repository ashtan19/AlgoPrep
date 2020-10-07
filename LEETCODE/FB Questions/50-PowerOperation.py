"""
Leetcode:50. Pow(x, n)

Attempts: 1
Completed: Y
Acheived Ideal: N
Under 30 Mins: Y

Time Complexity: O(logn)
Space Complexity: O(logn) if recursive but can be O(1)

Pattern: Iteration
Technique: get log n time by exploiting the trait that powers can be multiplied

Problems Encountered:
Other Solutions:

"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1/x
            n = -n

        def fastPow(x, n):
            if n == 0:
                return 1
            half = fastPow(x, n//2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        return fastPow(x, n)
