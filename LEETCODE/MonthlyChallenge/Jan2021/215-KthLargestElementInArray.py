"""
Leetcode: 215. Kth Largest Element in an Array

Attempts: 1
Completed: Y
Acheived Ideal: N
Under 30 Mins: Y

Time Complexity: O(nlogk)
Space Complexity: O(k)

Pattern: Kth largest
Technique: Minheap to keep track of k pargest elems

Problems Encountered:
Other Solutions: Quick select

"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq

        min_heap = []

        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
                continue

            if num > min_heap[0]:
                heapq.heapreplace(min_heap, num)

        return min_heap[0]
