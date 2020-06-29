"""
Question: Order-agnostic Binary Search (easy)

Time Complexity: O(logn)
Space Complexity: O(1)

Pattern: Binary Search
Technique: 

"""


def binary_search(arr, key):
    start, end = 0, len(arr) - 1
    isAscending = arr[start] < arr[end]
    while start <= end:
        # calculate the middle of the current range
        mid = start + (end - start) // 2

        if key == arr[mid]:
            return mid

        if isAscending:  # ascending order
            if key < arr[mid]:
                end = mid - 1  # the 'key' can be in the first half
            else:  # key > arr[mid]
                start = mid + 1  # the 'key' can be in the second half
        else:  # descending order
            if key > arr[mid]:
                end = mid - 1  # the 'key' can be in the first half
            else:  # key < arr[mid]
                start = mid + 1  # the 'key' can be in the second half

    return -1  # element not found

