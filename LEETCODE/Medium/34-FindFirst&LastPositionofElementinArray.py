"""
Leetcode: 34. Find First and Last Position of Element in Sorted Array

Attempts: 1 
Completed: Y 
Acheived Ideal: Yes

Time Complexity: O(logn)
Space Complexity: O(1)

Pattern: Binary Search 
Technique: Binary Search for upper and lower bounds

Problems Encountered: None 
Other Solutions: Linear Search but O(n) time 

"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == [] or nums == None:
            return [-1, -1]
        lowerBound = searchBounds(nums, target, True)
        if lowerBound == -1:
            return [-1, -1]
        upperBound = searchBounds(nums, target, False)

        return [lowerBound, upperBound]


def searchBounds(nums, target, isLowerBound):
    left, right = 0, len(nums) - 1
    foundTarget = False

    # First search to see if target is in nums
    while left <= right:
        mid = (right - left) // 2 + left
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            foundTarget = True
            if isLowerBound:
                right = mid - 1
            else:
                left = mid + 1

    if foundTarget == False:
        return -1
    if isLowerBound:
        return left
    else:
        return right

