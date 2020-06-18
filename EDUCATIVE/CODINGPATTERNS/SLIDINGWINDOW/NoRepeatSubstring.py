# Time Complexity: O(n)
# Space Complexity: O(1) b/c there are only 26 English letters

# Technique: Sliding Variable Window


def non_repeat_substring(str):
    char_count = {}
    result = 0
    window_start = 0

    for window_end in range(len(str)):
        new_char = str[window_end]
        while new_char in char_count:
            del char_count[str[window_start]]
            window_start += 1
        char_count[new_char] = True
        result = max(result, window_end-window_start+1)
    return result

# NO WHILE LOOP


def non_repeat_substring(str1):
    window_start = 0
    max_length = 0
    char_index_map = {}

    # try to extend the range [windowStart, windowEnd]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        # if the map already contains the 'right_char', shrink the window from the beginning so that
        # we have only one occurrence of 'right_char'
        if right_char in char_index_map:
            # this is tricky; in the current window, we will not have any 'right_char' after its previous index
            # and if 'window_start' is already ahead of the last index of 'right_char', we'll keep 'window_start'
            window_start = max(window_start, char_index_map[right_char] + 1)
        # insert the 'right_char' into the map
        char_index_map[right_char] = window_end
        # remember the maximum length so far
        max_length = max(max_length, window_end - window_start + 1)
    return max_length
