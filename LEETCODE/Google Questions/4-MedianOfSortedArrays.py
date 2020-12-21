"""
Leetcode: 4. Median of Two Sorted Arrays

Attempts: 1
Completed: Y
Acheived Ideal: N
Under 30 Mins: N

Time Complexity: O(log(min(m,n)))
Space Complexity: O(1)

Pattern: Sorted Array question
Technique: Special Technique uses binary search to find the partition for both arrays
            (https://www.youtube.com/watch?v=LPFhl65R7ww&feature=emb_logo)

Problems Encountered:
Other Solutions:

"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)

        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        total_len = m + n

        low = 0
        high = m

        while low <= high:
            partitionX = (low + high) / 2
            partitionY = (total_len + 1) / 2 - partitionX

            maxLeftX = nums1[partitionX -
                             1] if partitionX > 0 else -float("inf")
            minRightX = nums1[partitionX] if partitionX < m else float("inf")

            maxLeftY = nums2[partitionY -
                             1] if partitionY > 0 else -float("inf")
            minRightY = nums2[partitionY] if partitionY < n else float("inf")

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if total_len % 2 == 1:
                    return max(maxLeftX, maxLeftY)
                else:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2.0
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1
