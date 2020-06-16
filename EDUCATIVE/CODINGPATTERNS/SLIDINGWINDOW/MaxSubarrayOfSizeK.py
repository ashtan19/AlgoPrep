# Time Complexity: O(N)
# Space Complexity: O(1)


def max_sub_array_of_size_k(k, arr):
    # TODO: Write your code here
    maxSum = -float('inf')
    windowSum = 0
    windowStart = 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= k-1:
            maxSum = max(windowSum, maxSum)
            windowSum -= arr[windowStart]
            windowStart += 1
    return maxSum
