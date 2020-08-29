'''
Question: Maximum Ribbon Cuts

Time Complexity: O(n * total)
Space Complexity: O(n * total)

Pattern: DP Unbounded Knapsack
Technique: Take the max. Ensure that you initialize the dp to -inf

'''


def count_ribbon_pieces(ribbonLengths, total):
    n = len(ribbonLengths)
    dp = [[-float("inf") for _ in range(0, total+1)] for _ in range(0, n)]

    for i in range(0, n):
        for j in range(1, total + 1):
            cuts1, cuts2 = -float("inf"), -float("inf")
            if ribbonLengths[i] <= j:
                if j-ribbonLengths[i] == 0:
                    cuts1 = 1
                else:
                    cuts1 = dp[i][j-ribbonLengths[i]] + 1
            if i > 0:
                cuts2 = dp[i-1][j]
            dp[i][j] = max(cuts1, cuts2)

    return -1 if dp[n-1][total] < 0 else dp[n-1][total]
