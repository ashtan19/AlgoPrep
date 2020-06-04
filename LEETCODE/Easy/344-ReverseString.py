# Leetcode: 344 Reverse String (June Challenge Q)

# Attempts:1
# Completed:Y
# Acheived Ideal:Y

# Time Complexity:
# Space Complexity:

# Solving process:
# Problems Encountered:

# Other Solutions: python.reverse


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if s == '':
            return
        for i in range(len(s)/2):
            s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
