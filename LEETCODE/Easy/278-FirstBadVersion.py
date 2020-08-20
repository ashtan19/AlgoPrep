"""
Leetcode: 278. First Bad Version

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: log(n)
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
        left, right = 0, n

        while left <= right:
            mid = left + (right-left)//2

            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
