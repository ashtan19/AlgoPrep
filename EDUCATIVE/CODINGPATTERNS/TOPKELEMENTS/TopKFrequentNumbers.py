"""
Question: Top K Frequent Numbers

Time Complexity: O(n + nlogk)
Space Complexity: O(n + k)

Pattern: Top k Frequent Numbers 
Technique: Use a hashmap to record the frequency of each number and then use a min heap to filter out the 
            top k most frequent numbers

"""


from heapq import *
from collections import Counter


def find_k_frequent_numbers(nums, k):
    minheap = []
    # TODO: Write your code here
    numCount = Counter(nums)
    for num in numCount.keys():
        if len(minheap) < k:
            heappush(minheap, num)
        else:
            if numCount[num] > numCount[minheap[0]]:
                heappop(minheap)
                heappush(minheap, num)

    return minheap

