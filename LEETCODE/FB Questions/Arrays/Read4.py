
"""
Leetcode: 157. Read N Characters Given Read4

Attempts: 1
Completed: N
Acheived Ideal: N
Under 30 Mins: N

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Array Traversal 
Technique: 

Problems Encountered: 
Other Solutions:

"""


class Solution(object):
    def read(self, buf, n):
        copied_chars = 0
        read_chars = 4
        buf4 = [''] * 4

        while copied_chars < n and read_chars == 4:
            read_chars = read4(buf4)

            for i in range(read_chars):
                if copied_chars == n:
                    return copied_chars
                buf[copied_chars] = buf4[i]
                copied_chars += 1

        return copied_chars
