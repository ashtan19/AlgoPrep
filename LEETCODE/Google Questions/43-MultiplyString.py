"""
Leetcode: 43. Multiply Strings

Attempts: 1
Completed: N
Acheived Ideal: N
Under 30 Mins: N

Time Complexity: O(nm)
Space Complexity: O(n+m)

Pattern: Iteration
Technique: Follow the pattern when doing regular multiplication in math

Problems Encountered: maybe edge cases when adding numbers 
Other Solutions:

"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = [0] * (len(num1) + len(num2))
        position = len(result)-1

        for i in range(len(num1)-1, -1, -1):
            temp = position
            for j in range(len(num2)-1, -1, -1):
                result[temp] += int(num1[i]) * int(num2[j])
                result[temp-1] += result[temp] / 10
                result[temp] %= 10
                temp -= 1
            position -= 1

        k = 0
        while k < len(result)-1 and result[k] == 0:
            k += 1
        return "".join(map(str, result[k:]))
