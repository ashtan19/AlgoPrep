# Time Complexity: O(n)
# Space Complexity: O(1)

# Technique: Sliding Window


def smallest_subarray_with_given_sum(s, arr):
    # TODO: Write your code here
    smallestSub = len(arr)
    windowStart, windowSum = 0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        while windowSum >= s:
            smallestSub = min(smallestSub, windowEnd-windowStart+1)
            windowSum -= arr[windowStart]
            windowStart += 1
    return smallestSub
