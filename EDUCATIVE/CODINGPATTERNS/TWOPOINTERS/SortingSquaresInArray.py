# Time Complexity: O(n)
# Space Complexity: O(n)

# Technique: Two Pointer


def make_squares(arr):
    squares = [0 for x in range(len(arr))]
    end_index = len(arr)-1
    left = 0
    right = len(arr)-1

    while left <= right:
        left_square = arr[left]**2
        right_square = arr[right]**2
        if left_square > right_square:
            squares[end_index] = left_square
            left += 1
        else:
            squares[end_index] = right_square
            right -= 1
        end_index -= 1

    # TODO: Write your code here
    return squares
