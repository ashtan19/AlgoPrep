"""
Question: Kth Smallest Number

Time Complexity: O(n)
Space Complexity: O(k)

Pattern: Kth smallest Element 
Technique: Use a max heap with k elements 

"""


from heapq import *


def find_Kth_smallest_number(nums, k):
    # TODO: Write your code here
    max_heap = []
    for i in range(k):
        heappush(max_heap, -nums[i])

    for i in range(k, len(nums)):
        if nums[i] < -max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums[i])

    return -max_heap[0]
