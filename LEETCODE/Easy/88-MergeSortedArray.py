"""
Leetcode: 88 Merge Sorted Array

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(m+n)
Space Complexity: O(1)

Pattern: Two Pointer
Technique: Start from the back of both arrays and insert the larger number to back of nums1

Problems Encountered:
Other Solutions:

"""


'''
Inputs: 
- Two num arrays 
- num1 is is size m+n

Return: num1 sorted in place

nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Algorithm:
1) Initialize p1, p2, pEnd
2) While loop that iterates over elements from the back 
3) Compare which element is bigger and move it to pEnd 
4) Stop the loop when p2 < 0

nums1 = [1,2,2,3,5,6], m = 3
nums2 = [2,5,6],       n = 3

p1 = 1
p2 = -1
pEnd = 4
'''


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, pEnd = m-1, n-1, len(nums1)-1

        while p2 >= 0:
            num1 = nums1[p1] if p1 >= 0 else -float("inf")
            num2 = nums2[p2]
            if num1 >= num2:
                nums1[pEnd] = num1
                p1 -= 1
            else:
                nums1[pEnd] = num2
                p2 -= 1
            pEnd -= 1

        return nums1
