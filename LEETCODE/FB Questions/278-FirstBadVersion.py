"""
Leetcode: 278. First Bad Version

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(logn)
Space Complexity: O(1)

Pattern: Binary Search
Technique: 

Problems Encountered:
Other Solutions:

"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        l, r = 0, n

        while l < r:
            mid = l + (r-l)//2

            if isBadVersion(mid) == False:
                l = mid + 1
            else:
                r = mid

        return r
