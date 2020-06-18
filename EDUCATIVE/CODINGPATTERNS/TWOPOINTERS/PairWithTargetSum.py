# Time Complexity: O(n)
# Space Complexity: O(1)

# Technique: Two Pointer


def pair_with_targetsum(arr, target_sum):
    # TODO: Write your code here
    front = 0
    end = len(arr) - 1
    result = []
    while front <= end:
        curr_sum = arr[front] + arr[end]
        if curr_sum > target_sum:
            end -= 1
        elif curr_sum == target_sum:
            return [front, end]
        else:
            front += 1

    return [-1, -1]
