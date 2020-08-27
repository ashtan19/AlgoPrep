'''
Question: Rod Cutting

Time Complexity: O(n * C)
Space Complexity: O(n * C)

Pattern: DP Unbounded Knapsack
Technique: 

'''


def solve_rod_cutting(lengths, prices, n):
    lengthCount = len(lengths)
    # base checks
    dp = [[-1 for _ in range(0, n+1)] for _ in range(0, lengthCount)]

    for i in range(0, lengthCount):
        dp[i][0] = 0

    for i in range(0, lengthCount):
        for j in range(1, n+1):
            profit1, profit2 = 0, 0
            if lengths[i] <= j:
                profit1 = prices[i] + dp[i][j-lengths[i]]
            if i > 0:
                profit2 = dp[i-1][j]
            dp[i][j] = max(profit1, profit2)

    return dp[lengthCount-1][n]


def main():
    print(solve_rod_cutting([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))


main()
