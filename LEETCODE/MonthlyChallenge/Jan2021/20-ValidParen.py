"""
Leetcode:20. Valid Parentheses

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(n)
Space Complexity: O(n)

Pattern: Array and stacks
Technique: Use stack to keep track of bracket pairs

Problems Encountered:
Other Solutions:

"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        brackets = {")": "(", "]": "[", "}": "{"}
        stack = []

        for b in s:
            if b not in brackets:
                stack.append(b)
                continue

            open_b = brackets[b]
            if len(stack) == 0 or stack[-1] != open_b:
                return False

            stack.pop()

        return True if len(stack) == 0 else False
