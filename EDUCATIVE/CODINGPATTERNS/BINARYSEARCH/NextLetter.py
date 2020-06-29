"""
Question: Next Letter Circular List

Time Complexity: O(logn )
Space Complexity: O(1)

Pattern: Binary Search
Technique: 

"""


def search_next_letter(letters, key):
    # TODO: Write your code here
    if key >= letters[-1] or key < letters[0]:
        return letters[0]
    left, right = 0, len(letters) - 1
    while left <= right:
        mid = (right - left) // 2 + left
        if key == letters[mid]:
            return letters[mid + 1] if mid < len(letters) else letters[0]
        elif key < letters[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return letters[left] if left < len(letters) else letters[0]


def search_next_letter(letters, key):
    n = len(letters)
    if key < letters[0] or key > letters[n - 1]:
        return letters[0]

    start, end = 0, n - 1
    while start <= end:
        mid = start + (end - start) // 2
        if key < letters[mid]:
            end = mid - 1
        else:  # key >= letters[mid]:
            start = mid + 1

    # since the loop is running until 'start <= end', so at the end of the while loop, 'start == end+1'
    return letters[start % n]

