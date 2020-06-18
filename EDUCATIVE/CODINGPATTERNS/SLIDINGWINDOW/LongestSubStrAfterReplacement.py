# Time Complexity: O(n)
# Space Complexity: O(1) b/c there are only 26 English letters

# Technique: Sliding Variable Window


def length_of_longest_substring(str, k):
    # TODO: Write your code here
    if str == '' or str == None:
        return 0
    char_count = {}
    diff = 0
    window_start = 0
    cur_char = str[0]
    result = 0

    for window_end in range(len(str)):
        new_char = str[window_end]
        char_count[new_char] = char_count.get(new_char, 0) + 1
        while window_end-window_start + 1 - char_count[cur_char] > k:
            while str[window_start] == cur_char:
                window_start += 1
                char_count[cur_char] -= 1
            cur_char = str[window_start]
        result = max(result, window_end-window_start+1)

    return result


# NO WHILE LOOP
def length_of_longest_substring(str1, k):
    window_start, max_length, max_repeat_letter_count = 0, 0, 0
    frequency_map = {}

    # Try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in frequency_map:
            frequency_map[right_char] = 0
        frequency_map[right_char] += 1
        max_repeat_letter_count = max(
            max_repeat_letter_count, frequency_map[right_char])

        # Current window size is from window_start to window_end, overall we have a letter which is
        # repeating 'max_repeat_letter_count' times, this means we can have a window which has one letter
        # repeating 'max_repeat_letter_count' times and the remaining letters we should replace.
        # if the remaining letters are more than 'k', it is the time to shrink the window as we
        # are not allowed to replace more than 'k' letters
        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            left_char = str1[window_start]
            frequency_map[left_char] -= 1
            window_start += 1

        max_length = max(max_repeat_letter_count,
                         window_end - window_start + 1)
    return max_length
