# Time Complexity: O(n)
# Space Complexity: O(1)

# Technique: Two Pointer


def remove_duplicates(arr):
    # TODO: Write your code here
    if arr == None:
        return 0
    if len(arr) == 1:
        return 1

    end_of_non_duplicates = 1

    for i in range(1, len(arr)):
        if arr[i] != arr[end_of_non_duplicates-1]:
            arr[end_of_non_duplicates] = arr[i]
            end_of_non_duplicates += 1

    return end_of_non_duplicates
