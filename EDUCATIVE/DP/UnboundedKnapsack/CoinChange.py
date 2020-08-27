'''
Question: Coin Change

Time Complexity: O(n * C)
Space Complexity: O(n * C)

Pattern: DP Unbounded Knapsack
Technique: Make sure to seed the first column with one 

'''


def count_change(denominations, total):
    n = len(denominations)
    dp = [[0 for _ in range(0, total + 1)] for _ in range(0, n)]

    for i in range(0, n):
        dp[i][0] = 1

    for i in range(0, n):
        for j in range(1, total + 1):
            coinIncluded, notIncluded = 0, 0
            if denominations[i] <= j:
                coinIncluded = dp[i][j-denominations[i]]
            if i > 0:
                notIncluded = dp[i-1][j]
            dp[i][j] = coinIncluded + notIncluded

    print(dp)

    return dp[n-1][total]
