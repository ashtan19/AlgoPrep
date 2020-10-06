"""
Leetcode: 33. Search in Rotated Sorted Array

Attempts: 1
Completed: Y
Acheived Ideal: N but close
Under 30 Mins: Y

Time Complexity: O(logn)
Space Complexity: O(1)

Pattern: Binary Search 
Technique: My Technique is first to find the pivot then search the part of the array that may contain the target

Problems Encountered:
Other Solutions: One pass Binary Search: Check if the first half of the array contains the pivot. If it does not, so a regular B-search on it


"""

# One pass solution


class Solution:
    def search(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

# Original Two pass solution


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def b_search(arr, target):
            l, r = 0, len(arr)-1
            while l <= r:
                mid = l + (r-l)//2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        def find_pivot(arr):
            l, r = 0, len(arr)-1
            while l <= r:
                mid = l + (r-l)//2
                if arr[mid] > arr[-1]:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        pivot = find_pivot(nums)
        print(pivot)
        if target <= nums[-1]:
            index = b_search(nums[pivot:], target)
            return pivot + index if index != -1 else -1
        else:
            return b_search(nums[:pivot+1], target)
