"""
Question: Minimum Difference Element

Time Complexity: O(logn)
Space Complexity: O(1)

Pattern: Binary Search
Technique: Do a binary search and return the value if it matches
            If the element is not in the array, then the left amd right
            indexes will be the closest to element

"""


def search_min_diff_element(arr, key):
    # TODO: Write your code here
    if key < arr[0]:
        return arr[0]
    if key > arr[-1]:
        return arr[-1]

    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if key < arr[mid]:
            right = mid - 1
        elif key > arr[mid]:
            left = mid + 1
        else:
            return arr[mid]

    if (arr[left] - key) < (key - arr[right]):
        return arr[left]
    return arr[right]

