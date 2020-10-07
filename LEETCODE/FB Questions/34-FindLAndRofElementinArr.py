"""
Leetcode: 34. Find First and Last Position of Element in Sorted Array

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(logn)
Space Complexity: O(1)

Pattern: Binary Search
Technique: Find the lower bound and the upper bound 

Problems Encountered:
Other Solutions:

"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if nums == None or nums == []:
            return [-1, -1]

        def searchBoundary(nums, target, isLeft):
            l, r = 0, len(nums)-1

            while l <= r:
                mid = l + (r-l)//2
                if nums[mid] == target:
                    if isLeft and mid != 0 and nums[mid-1] == target:
                        r = mid - 1
                    elif not isLeft and mid != len(nums)-1 and nums[mid+1] == target:
                        l = mid + 1
                    else:
                        return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        left_bound = searchBoundary(nums, target, True)
        right_bound = searchBoundary(nums, target, False)

        return [left_bound, right_bound]
