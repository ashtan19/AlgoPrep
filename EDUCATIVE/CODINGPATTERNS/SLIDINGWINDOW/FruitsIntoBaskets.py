# Time Complexity: O(n+n)
# Space Complexity: O(k)

# Technique: Sliding Variable Window


def fruits_into_baskets(fruits):
    # TODO: Write your code here
    fruit_freq = {}
    window_start = 0
    result = 0
    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        fruit_freq[right_fruit] = fruit_freq.get(right_fruit, 0) + 1

        if len(fruit_freq) > 2:
            while len(fruit_freq) > 2:
                left_fruit = fruits[window_start]
                fruit_freq[left_fruit] -= 1
                if fruit_freq[left_fruit] == 0:
                    del fruit_freq[left_fruit]
                window_start += 1

        result = max(result, window_end-window_start+1)

    return result
