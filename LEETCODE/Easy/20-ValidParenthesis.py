# Leetcode: 20 Valid Parentheses

# Attempt: 2

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

# Attempt 2


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        brackets = {"}": "{", "]": "[", ")": "("}

        for b in s:
            if b == "{" or b == "[" or b == "(":
                stack.append(b)
            else:
                if stack == [] or stack.pop() != brackets[b]:
                    return False

        return stack == []
