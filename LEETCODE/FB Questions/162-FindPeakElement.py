"""
Leetcode: 162. Find Peak Element

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(logn)
Space Complexity: O(1)

Pattern: Binary Search
Technique: Check the slope

Problems Encountered:
Other Solutions: You optimize by checking only the left adj

"""


'''
algorithm:
- Start a binary search. 
- Get middle element, and left adj, right adj. Set adj to -inf if index == -1 or n
- If middle element is greater than left but smaller than right -> l = mid + 1 (Slope to right)
- If slope to left then r = mid - 1
- If mid element is min => go to right (arbitrary because there will be maxs on both sides)


[1,2,1,3,5,6]

'''


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l, r = 0, n-1

        while l <= r:
            mid = l + (r-l)//2
            left_adj = nums[mid-1] if (mid > 0) else -float("inf")
            right_adj = nums[mid+1] if (mid < n-1) else -float("inf")

            if nums[mid] > left_adj and nums[mid] > right_adj:
                return mid
            elif nums[mid] < left_adj and nums[mid] > right_adj:
                r = mid - 1
            else:
                l = mid + 1

# Solution with only one check


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l, r = 0, n-1

        while l < r:
            mid = l + (r-l)//2

            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1
        return l
