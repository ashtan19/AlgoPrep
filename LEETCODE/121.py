# Leetcode: 121 Best Time to Buy Stock

# Time Complexity: O(n^2) - Bad, O(n)
# Space Complexity: O(1)
# Solving process:
# Problems Encountered:

# Other Solutions: Keep a variable for min price and a variable for max profit, as you iterate, if you find a new smaller min -update
# Then continue comparing with current values to find max profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        if len(prices) <= 1:
            return max
        for i in range(0, len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > max:
                    max = prices[j] - prices[i]
        return max


def maxProfit(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit
