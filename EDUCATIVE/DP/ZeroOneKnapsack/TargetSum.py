'''
Question: Target Sum

Time Complexity: O(n * Sum)
Space Complexity: O(Sum)

Pattern: DP 0/1 Knapsack
Technique: test test

'''


def find_target_subsets(num, s):
  totalSum = sum(num)

  # if 's + totalSum' is odd, we can't find a subset with sum equal to '(s + totalSum) / 2'
  if totalSum < s or (s + totalSum) % 2 == 1:
    return 0

  return count_subsets(num, int((s + totalSum) / 2))


# this function is exactly similar to what we have in 'Count of Subset Sum' problem.
def count_subsets(num, s):
  n = len(num)
  dp = [[0 for x in range(s+1)] for y in range(n)]

  # populate the sum = 0 columns, as we will always have an empty set for zero sum
  for i in range(0, n):
    dp[i][0] = 1

  # with only one number, we can form a subset only when the required sum is
  # equal to the number
  for s in range(1, s+1):
    dp[0][s] = 1 if num[0] == s else 0

  # process all subsets for all sums
  for i in range(1, n):
    for s in range(1, s+1):
      dp[i][s] = dp[i - 1][s]
      if s >= num[i]:
        dp[i][s] += dp[i - 1][s - num[i]]

  # the bottom-right corner will have our answer.
  return dp[n - 1][s]
