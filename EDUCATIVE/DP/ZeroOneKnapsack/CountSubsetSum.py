'''
Question: Count of Subset Sum

Time Complexity: O(n * sum)
Space Complexity: O(n * sum)

Pattern: DP 0/1 Knapsack
Technique: Have the dp keep track of the number of subsets that can be made for that sum

'''


def count_subsets(num, sum):
    n = len(num)
    dp = [[0 for x in range(0, sum+1)] for y in range(0, n)]

    for j in range(0, sum+1):
        dp[0][j] = 1 if num[0] == j else 0

    for i in range(0, n):
        dp[i][0] = 1

    for i in range(1, n):
        for j in range(1, sum+1):
            dp[i][j] = dp[i-1][j]
            if j >= num[i]:
                dp[i][j] += dp[i-1][j-num[i]]
    print(dp)
    return dp[n-1][sum]

# Solution O(sum) space
    def count_subsets(num, sum):
    n = len(num)
    dp = [0 for x in range(0, sum+1)]

    for j in range(0, sum+1):
        dp[j] = 1 if num[0] == j else 0

    dp[0] = 1

    for i in range(1, n):
        for j in range(sum, -1, -1):
            if j >= num[i]:
                dp[j] += dp[j-num[i]]
    print(dp)
    return dp[sum]
