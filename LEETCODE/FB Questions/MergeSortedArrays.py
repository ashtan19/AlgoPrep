"""
Leetcode: 88. Merge Sorted Array

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(n+m)
Space Complexity: O(1)

Pattern: Two Pointer
Technique: Start from the end 

Problems Encountered:
Other Solutions:

"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        totalLen = len(nums1)
        curPointer = totalLen-1

        while m > 0 or n > 0:
            val1 = nums1[m-1] if m > 0 else -float("inf")
            val2 = nums2[n-1] if n > 0 else -float("inf")

            if val1 >= val2:
                nums1[curPointer] = val1
                m -= 1
            else:
                nums1[curPointer] = val2
                n -= 1
            curPointer -= 1
