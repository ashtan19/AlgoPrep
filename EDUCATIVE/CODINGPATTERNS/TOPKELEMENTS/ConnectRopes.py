"""
Question: Connect Ropes 

Time Complexity: O(nlogn)
Space Complexity: O(n)

Pattern: Top K Elements
Technique: Use a heap to extract the smallest elements 

"""


from heapq import *


def minimum_cost_to_connect_ropes(ropeLengths):
    minheap = []
    # TODO: Write your code here
    for rope in ropeLengths:
        heappush(minheap, rope)

    cost, curcost = 0, 0
    while len(minheap) > 1:
        curcost = heappop(minheap) + heappop(minheap)
        cost += curcost
        heappush(minheap, curcost)

    return cost

