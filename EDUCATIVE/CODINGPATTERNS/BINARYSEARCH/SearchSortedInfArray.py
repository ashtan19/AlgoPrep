"""
Question: Search in a Sorted Infinite Array (medium)



Time Complexity: O(logn)
Space Complexity: O(1)

Pattern: BFS
Technique: First find the start and end range that you should do the 
            binary search on.

"""


import math


class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def search_in_infinite_array(reader, key):
    # TODO: Write your code here
    previndex, curindex = 0, 1

    while reader.get(curindex) < key:
        newprev = curindex + 1
        curindex = (curindex - previndex + 1) * 2
        previndex = newprev
        # curindex = curindex * 2
        # previndex = curindex

    while previndex <= curindex:
        mid = (curindex - previndex) // 2 + previndex
        if reader.get(mid) == math.inf or key < reader.get(mid):
            curindex = mid - 1
        elif key > reader.get(mid):
            previndex = mid + 1
        else:
            return mid

    return -1

