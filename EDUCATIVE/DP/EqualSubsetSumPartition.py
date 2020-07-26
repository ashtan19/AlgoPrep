
'''
Question: Equal Subset Sum Partition

Time Complexity: O(n * sum)
Space Complexity: O(n * sum)

Pattern: DP 0/1 Knapsack
Technique: Use a True/False DP matrix to see if you can reach zero Sum 

'''


def can_partition(num):
  # TODO: Write your code here
  if not num or len(num) == 0:
    return False
  n = len(num)
  numSum = sum(num)
  if numSum % 2 == 1:
    return False
  halfSum = numSum // 2

  dp = [[False for x in range(halfSum+1)] for y in range(n)] 

  for i in range(n):
    dp[i][0] = True

  for c in range(halfSum +1):
    if num[0] == c:
      dp[0][c] == True

  for i in range(1, n):
    for c in range(1, halfSum + 1):
      canZero1, canZero2 = False, False
      if num[i] <= c:
        canZero1 = dp[i-1][c-num[i]]
      canZero2 = dp[i-1][c]
      dp[i][c] = canZero1 or canZero2
  
  
  return dp[n-1][halfSum]
