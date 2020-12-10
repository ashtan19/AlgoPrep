

"""
Leetcode: 394. Decode String

Attempts: 1
Completed: Y
Acheived Ideal: Y but could be cleaner code
Under 30 Mins: Y

Time Complexity: 
Space Complexity: 

Pattern: String and Array 
Technique: Use stack to keep track of the count 

Problems Encountered:
Other Solutions:

"""


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        result = []

        n = len(s)
        i = 0
        repeats = []
        number = []
        encoded = []

        while i < n:
            c = s[i]
            if c == "[":
                count = int("".join(number))
                repeats.append((count, encoded[:]))
                encoded, number = [], []
            elif c == "]":
                count, pre = repeats.pop()
                encoded = pre + encoded * count

            elif c.isalpha():
                encoded.append(c)
            elif c.isdigit():
                number.append(c)

            i += 1

        return "".join(encoded)

# Cleaner solution with stack


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
