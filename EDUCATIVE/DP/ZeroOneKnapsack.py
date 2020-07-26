'''
Question: 0/1 Knapsack

Time Complexity: O(n * c)
Space Complexity: O(n * c) => could be O(c) if you just use one array

Pattern: DP 0/1 Knapsack
Technique: Bottom Up Tabulation

'''


def solve_knapsack(profits, weights, capacity):
  # TODO: Write - Your - Code
  n = len(profits)
  if capacity <= 0 or n == 0 or len(weights) != n:
    return 0

  dp = [[0 for x in range(capacity+1)] for y in range(n)]

  for i in range(0, n):
    dp[i][0] = 0

  for c in range(capacity+1):
    if weights[0] <= c:
      dp[0][c] = profits[0]

  for i in range(1, n):
    for c in range(1, capacity+1):
      profit1, profit2 = 0,0
      if weights[i] <= c:
        profit1 = profits[i] + dp[i-1][c - weights[i]]
      profit2 = dp[i-1][c]
      dp[i][c] = max(profit1, profit2)

  return dp[n-1][capacity];


  def print_selected_elements(dp, weights, profits, capacity):
  print("Selected weights are: ", end='')
  n = len(weights)
  totalProfit = dp[n-1][capacity]
  for i in range(n-1, 0, -1):
    if totalProfit != dp[i - 1][capacity]:
      print(str(weights[i]) + " ", end='')
      capacity -= weights[i]
      totalProfit -= profits[i]

  if totalProfit != 0:
    print(str(weights[0]) + " ", end='')
  print()