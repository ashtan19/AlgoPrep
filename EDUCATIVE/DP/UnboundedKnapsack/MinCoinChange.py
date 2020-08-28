'''
Question: Minimum Coin Change



Time Complexity: O(n * C)
Space Complexity: O(n * C)

Pattern: DP Unbounded Knapsack
Technique: Track the min. Make sure that you add 1

'''


def count_change(denominations, total):
    n = len(denominations)
    dp = [[float("inf") for _ in range(0, total + 1)] for _ in range(0, n)]

    for i in range(0, n):
        dp[1][0] = 0

    for i in range(0, n):
        for j in range(1, total + 1):
            minChange1, minChange2 = float("inf"), float("inf")
            if denominations[i] <= j:
                minChange1 = dp[i][j-denominations[i]] + 1
            if i > 0:
                minChange2 = dp[i-1][j]
            dp[i][j] = min(minChange1, minChange2)

    return dp[n-1][total]


def main():
    print(count_change([1, 2, 3], 5))
    print(count_change([1, 2, 3], 11))
    print(count_change([1, 2, 3], 7))
    print(count_change([3, 5], 7))


main()
