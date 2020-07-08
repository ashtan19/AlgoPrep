"""
Question: Kth Smallest Number in M Sorted Lists (Medium)

Time Complexity: O(klogm)
Space Complexity: O(M)

Pattern: Two Pointer
Technique: We have a minheap for the min of the interables (size M), in the heap we store a tuple. Keep a count up to K then we return

"""

# O(klogm) Solution => Do not have to go through all elements just up to k
from heapq import *


def find_Kth_smallest(lists, k):
    minheap = []

    # TODO: Write your code here
    for i in range(len(lists)):
        if len(lists[i]) > 0:
            heappush(minheap, (lists[i][0], 0, lists[i]))

    number, currentCount = 0, 0
    while minheap:
        number, i, list = heappop(minheap)
        currentCount += 1
        if currentCount == k:
            break
        if i + 1 < len(list):
            heappush(minheap, (list[i + 1], i + 1, list))

    return number


# nlogk solution
from heapq import *


def find_Kth_smallest(lists, k):
    maxheap = []
    for list in lists:
        for num in list:
            if len(maxheap) == k:
                if num < -maxheap[0]:
                    heappop(maxheap)
                    heappush(maxheap, -num)
            else:
                heappush(maxheap, -num)

    return -maxheap[0]

