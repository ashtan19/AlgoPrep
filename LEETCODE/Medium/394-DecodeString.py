# Leetcode: 394. Decode String

# Completed: N
# Acheived Ideal:

# Time Complexity: O(n)
# Space Complexity: O(n)

# Solving process: Use a stack
# Problems Encountered:

# Other Solutions:



class Solution(object):
    def decodeString(self, s):
        stack = []
        stack.append(["", 1])
        num = ""
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == '[':
                stack.append(["", int(num)])
                num = ""
            elif ch == ']':
                st, k = stack.pop()
                stack[-1][0] += st*k
            else:
                stack[-1][0] += ch
        return stack[0][0]
