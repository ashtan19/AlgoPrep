"""
Question: Ceiling Number

Time Complexity: O(logn)
Space Complexity: O(1)

Pattern: Binary Search
Technique: 

test test

"""


def search_ceiling_of_a_number(arr, key):
    n = len(arr)
    if key > arr[n - 1]:  # if the 'key' is bigger than the biggest element
        return -1

    start, end = 0, n - 1
    while start <= end:
        mid = start + (end - start) // 2
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:  # found the key
            return mid

    # since the loop is running until 'start <= end', so at the end of the while loop, 'start == end+1'
    # we are not able to find the element in the given array, so the next big number will be arr[start]
    return start

