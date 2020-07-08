"""
Question: Kth Largest Number in a Stream (medium)

Time Complexity: O(nlogk)
Space Complexity: O(k)

Pattern: Top K Elements 
Technique: Same 

"""


from heapq import heappush, heappop


class KthLargestNumberInStream:
    def __init__(self, nums, k):
        # TODO: Write your code here
        self.min_heap = []
        for i in range(k):
            heappush(self.min_heap, nums[i])

        for i in range(k, len(nums)):
            if nums[i] > self.min_heap[0]:
                heappop(self.min_heap)
                heappush(self.min_heap, nums[i])
        self.k = k

    def add(self, num):
        # TODO: Write your code here
        if num > self.min_heap[0]:
            heappop(self.min_heap)
            heappush(self.min_heap, num)
        return self.min_heap[0]

