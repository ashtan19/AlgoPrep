'''
Question: Subset Sum

Time Complexity: O(n * S)
Space Complexity: O(n * S)

Pattern: DP 0/1 Knapsack
Technique: Use a T/F matrix. Could include early termination of you reach sum and it is true

'''

def can_partition(num, sum):
  n = len(num)
  dp = [[False for x in range(sum+1)] for y in range(n)]

  # populate the sum = 0 columns, as we can always form '0' sum with an empty set
  for i in range(0, n):
    dp[i][0] = True

  # with only one number, we can form a subset only when the required sum is
  # equal to its value
  for s in range(1, sum+1):
    dp[0][s] = True if num[0] == s else False

  # process all subsets for all sums
  for i in range(1, n):
    for s in range(1, sum+1):
      # if we can get the sum 's' without the number at index 'i'
      if dp[i - 1][s]:
        dp[i][s] = dp[i - 1][s]
      elif s >= num[i]:
        # else include the number and see if we can find a subset to get the remaining sum
        dp[i][s] = dp[i - 1][s - num[i]]

  # the bottom-right corner will have our answer.
  return dp[n - 1][sum]