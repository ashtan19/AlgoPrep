# Time Complexity: O(n)
# Space Complexity: O(1)

# Technique: Two Pointer


def remove_element(arr, key):
    nextElement = 0  # index of the next element which is not 'key'
    for i in range(len(arr)):
        if arr[i] != key:
            arr[nextElement] = arr[i]
            nextElement += 1

    return nextElement
