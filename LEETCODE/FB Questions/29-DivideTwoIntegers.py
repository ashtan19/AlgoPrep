"""
Leetcode: 29. Divide Two Integers

Attempts: 1
Completed: Y
Acheived Ideal: N
Under 30 Mins: Y

Time Complexity: O(log(dividend))
Space Complexity: O(1)

Pattern: Bit Manipulation
Technique: Shift to the divisor to the largest size that would fit in the dividend, then subtract from dividend and 
            add 1 << i to the result because the rounded value division of dividend and divisor << i is 1<<i

Problems Encountered:
Other Solutions: Iterative approach but very slow

"""

# Solution with bit manipulation


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
        if dividend == -2**31 and divisor == -1:
            return 2**31-1
        result = 0
        dividend = abs(dividend)
        divisor = abs(divisor)

        for i in range(31, -1, -1):
            if dividend >= divisor << i:
                dividend -= divisor << i
                result += 1 << i

        return sign * result


# Brute Force Approach
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
        i = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            dividend -= divisor
            i += 1

        return i * sign
