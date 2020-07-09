"""
Question: Kth Smallest Number in a Sorted Matrix (Hard)

Time Complexity: O(klogk)
Space Complexity: O(k)

Pattern: Two Pointer
Technique: 

"""


from heapq import *


def find_Kth_smallest(matrix, k):
    number = -1
    # TODO: Write your code here
    minheap = []
    numbercount = 0
    for i in range(min(k, len(matrix))):
        heappush(minheap, (matrix[i][0], 0, matrix[i]))

    while minheap:
        value, index, array = heappop(minheap)
        numbercount += 1
        number = value
        if numbercount == k:
            break
        if index + 1 < len(array):
            heappush(minheap, (array[index + 1], index + 1, array))
    return number

