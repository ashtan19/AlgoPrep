# Leetcode: 215 Kth Largest Element in an Array

# Completed:        Yes
# Acheived Ideal:   No

# Time Complexity:  O(nlogn) O(n)
# Space Complexity: O(1)    O(n^2)

# Solving process:
# Problems Encountered:

# Other Solutions:  Use Quicksort-Partition Method


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        return sorted(nums)[len(nums)-k]


class Solution(object):
    # O(n) time, quicksort-Partition method
    def findKthLargest(self, nums, k):
        pos = self.partition(nums, 0, len(nums)-1)
        if pos > len(nums) - k:
            return self.findKthLargest(nums[:pos], k-(len(nums)-pos))
        elif pos < len(nums) - k:
            return self.findKthLargest(nums[pos+1:], k)
        else:
            return nums[pos]

    # Lomuto partition scheme
    def partition(self, nums, l, r):
        index = random.randint(0, len(nums) - 1)
        nums[index], nums[r] = nums[r], nums[index]
        pivot = nums[r]
        lo = l
        for i in xrange(l, r):
            if nums[i] < pivot:
                nums[i], nums[lo] = nums[lo], nums[i]
                lo += 1
        nums[lo], nums[r] = nums[r], nums[lo]
        return lo
