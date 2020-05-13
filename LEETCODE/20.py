# Leetcode: 20 Valid Parentheses

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solving process: Keep a stack of the open brackets, when you encounter a closing bracket, compare with top of stack
# Problems Encountered:

# Other Solutions:


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        brackets = {"}": "{", "]": "[", ")": "("}

        for brac in s:
            if brac in brackets.values():
                stack.append(brac)
            elif brac in brackets:
                if stack == [] or brackets[brac] != stack.pop():
                    return False
            else:
                return False

        return stack == []
