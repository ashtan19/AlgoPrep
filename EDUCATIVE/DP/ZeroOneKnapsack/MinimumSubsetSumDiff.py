'''
Question: Minimum Subset Sum Difference

Time Complexity: O(n * halfSum)
Space Complexity: O(n * halfSum)

Pattern: DP 0/1 Knapsack
Technique: Do a subset sum, check for the close sum to halfsum

'''


def can_partition(num):
    s = sum(num)
    n = len(num)
    halfSum = int(s // 2)

    dp = [[False for x in range(0, halfSum + 1)] for y in range(0, n)]

    for i in range(0, n):
        dp[i][0] = True

    for j in range(0, halfSum + 1):
        dp[0][j] = num[0] == j

    for i in range(1, n):
        for j in range(1, halfSum+1):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i-1][j-num[i]]

    sum1 = 0
    sum2 = 0
    for j in range(halfSum, -1, -1):
        if dp[n-1][j]:
            sum1 = j
            break

    sum2 = s - sum1
    return abs(sum1 - sum2)
