"""
Leetcode:32. Longest Valid Parentheses

Attempts: 1
Completed: N
Acheived Ideal: Y
Under 30 Mins: N

Time Complexity: O(n)
Space Complexity: O(n)

Pattern: DP
Technique: Using a stack to remember of the last index that was invalid

Problems Encountered:
Other Solutions: O(1) space solution using a two pass method 

"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_len, stack = 0, [-1]

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack_top = s[stack[-1]] if len(stack) > 1 else ")"
                if stack_top == ")":
                    stack.append(i)
                else:
                    stack.pop()
                    max_len = max(i-stack[-1], max_len)

        return max_len


# O(n) time and O(1) space
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_len, left, right = 0, 0, 0

        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            else:
                right += 1

            if left == right:
                max_len = max(max_len, 2 * right)
            elif right >= left:
                left = right = 0

        left = right = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1

            if left == right:
                max_len = max(max_len, 2 * left)
            elif left >= right:
                left = right = 0

        return max_len
