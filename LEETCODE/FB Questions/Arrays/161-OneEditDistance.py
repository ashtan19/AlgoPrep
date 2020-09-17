
"""
Leetcode: 161. One Edit Distance

Attempts: 1
Completed: N 
Acheived Ideal: N
Under 30 Mins: N

Time Complexity: O(n)
Space Complexity: O(n)

Pattern: Array Traversal 
Technique: 

Problems Encountered:
Other Solutions:

"""


class Solution:
    def isOneEditDistance(self, s, t):
        sl, tl = len(s), len(t)

        if abs(sl-tl) > 1:
            return False

        for i in range(0, min(sl, tl)):
            if s[i] != t[i]:
                if sl == tl:
                    return s[i+1:] == t[i+1:]
                if sl > tl:
                    return s[i+1:] == t[i:]
                else:
                    return s[i:] == t[i+1:]

        return abs(sl-tl) == 1
