# Leetcode: 540 Single Element in a Sorted Array

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solving process:
# Problems Encountered:

# Other Solutions: For O(logn), we need to do binary search based on the fact that if element i is before the pivot element
#                   then it should have a duplicate element at i+1. if not then move to right

# O(n) Iterative Solution


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if i == len(nums)-1:
                return nums[-1]
            if nums[i] != nums[i+1]:
                if nums[i+2] == nums[i+1]:
                    return nums[i]
                else:
                    return num[i+1]
            i += 2

        return -1


def singleNonDuplicate(self, nums: List[int]) -> int:
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = 2 * ((lo + hi) // 4)
        if nums[mid] == nums[mid+1]:
            lo = mid+2
        else:
            hi = mid
    return nums[lo]
