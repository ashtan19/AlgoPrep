'''
Question: Triplet Sum Close to Target (medium)

Time Complexity: O(n^2)
Space Complexity: O(n)

Pattern: Two Pointer
Technique: Triple Pointer. With Searching for Pair Sum. However, you note the pair that gives you the 
            smallest difference and closest sum


'''


def triplet_sum_close_to_target(arr, target_sum):
    # TODO: Write your code here
    arr.sort()
    closest_sum = float('inf')
    smallest_difference = float('inf')

    for i in range(len(arr)):
        right = len(arr)-1
        left = i+1
        cur_value = arr[i]
        while left < right:
            curr_sum = cur_value + arr[left] + arr[right]
            if curr_sum < target_sum:
                left += 1
            else:
                right -= 1
            if abs(target_sum - curr_sum) < smallest_difference:
                smallest_difference = abs(target_sum - curr_sum)
                closest_sum = curr_sum

    return closest_sum
