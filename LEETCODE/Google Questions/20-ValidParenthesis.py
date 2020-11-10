"""
Leetcode: 20. Valid Parentheses

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(n)
Space Complexity: O(n)

Pattern: Stack
Technique: Use stack to keep track of closing brackets 

Problems Encountered:
Other Solutions:

"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        brackets = {'{': '}', '(': ')', '[': ']'}
        openers = set({"{", "(", "["})

        stack = []

        for c in s:
            if c in openers:
                stack.append(brackets[c])
                continue

            if len(stack) == 0 or stack[-1] != c:
                return False

            stack.pop()

        return True if len(stack) == 0 else False
