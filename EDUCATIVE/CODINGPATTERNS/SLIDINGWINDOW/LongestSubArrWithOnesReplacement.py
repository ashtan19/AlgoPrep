# Time Complexity: O(n)
# Space Complexity: O(1)

# Technique: Sliding Variable Window


def length_of_longest_substring(arr, k):
    # TODO: Write your code here
    maxcount, max_len, ones, window_start = 0, 0, 0, 0

    for window_end in range(len(arr)):
        new_num = arr[window_end]
        if new_num == 1:
            ones += 1

        if window_end - window_start + 1 - ones > k:
            last_char = arr[window_start]
            if last_char == 1:
                ones -= 1
            window_start += 1

        max_len = max(max_len, window_end-window_start+1)

    return max_len
