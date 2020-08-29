'''
Question: Staircase

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Fibonacci
Technique: 

'''

# Bottom Up with O(1) space


def count_ways(n):
    if n < 2:
        return 1
    if n == 2:
        return 2
    n1, n2, n3 = 1, 1, 2
    for i in range(3, n+1):
        n1, n2, n3 = n2, n3, n1+n2+n3
    return n3


# Bottom Up
def count_ways(n):
    dp = [0 for x in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]

# Recursive Top Down


def count_ways(n):
    dp = [0 for x in range(n+1)]
    return count_ways_recursive(dp, n)


def count_ways_recursive(dp, n):
    if n == 0:
        return 1  # base case, we don't need to take any step, so there is only one way

    if n == 1:
        return 1  # we can take one step to reach the end, and that is the only way

    if n == 2:
        return 2  # we can take one step twice or jump two steps to reach at the top

    if dp[n] == 0:
        # if we take 1 step, we are left with 'n-1' steps;
        take1Step = count_ways_recursive(dp, n - 1)
        # similarly, if we took 2 steps, we are left with 'n-2' steps;
        take2Step = count_ways_recursive(dp, n - 2)
        # if we took 3 steps, we are left with 'n-3' steps;
        take3Step = count_ways_recursive(dp, n - 3)

        dp[n] = take1Step + take2Step + take3Step

    return dp[n]
