"""
Question: Number Range Binary Search 

Time Complexity: O(logn)
Space Complexity: O(1)

Pattern: Binary Search
Technique: 

"""


def find_range(arr, key):
    result = [-1, -1]
    # TODO: Write your code here
    result[1] = binarySearch(arr, key, True)
    if result[1] != -1:
        result[0] = binarySearch(arr, key, False)
    return result


def binarySearch(arr, key, findmaxrange):
    left, right, keyindex = 0, len(arr) - 1, -1
    while left <= right:
        mid = (right - left) // 2 + left
        if key < arr[mid]:
            right = mid - 1
        elif key > arr[mid]:
            left = mid + 1
        else:
            keyindex = mid
            if findmaxrange:
                left = mid + 1
            else:
                right = mid - 1
    return keyindex

