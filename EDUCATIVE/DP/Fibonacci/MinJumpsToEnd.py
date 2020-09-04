'''
Question: 

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Fibonacci
Technique: 

'''


import math


def count_min_jumps(jumps):
    dp = [0 for x in range(len(jumps))]
    return count_min_jumps_recursive(dp, jumps, 0)


def count_min_jumps_recursive(dp, jumps, currentIndex):
    n = len(jumps)
    # if we have reached the last index, we don't need any more jumps
    if currentIndex == n - 1:
        return 0

    if jumps[currentIndex] == 0:
        return math.inf

    # if we have already solved this problem, return the result
    if dp[currentIndex] != 0:
        return dp[currentIndex]

    totalJumps = math.inf
    start, end = currentIndex + 1, currentIndex + jumps[currentIndex]
    while start < n and start <= end:
        # jump one step and recurse for the remaining array
        minJumps = count_min_jumps_recursive(dp, jumps, start)
        start += 1
        if minJumps != math.inf:
            totalJumps = min(totalJumps, minJumps + 1)

    dp[currentIndex] = totalJumps
    return dp[currentIndex]


def main():

    print(count_min_jumps([2, 1, 1, 1, 4]))
    print(count_min_jumps([1, 1, 3, 6, 9, 3, 0, 1, 3]))


main()
