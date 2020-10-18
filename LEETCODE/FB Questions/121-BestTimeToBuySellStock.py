"""
Leetcode: 121 Best Time to buy and sell stock

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: Y

Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Array 
Technique: Track current min value

Problems Encountered:
Other Solutions:

"""


'''
Idea:
- Track the current min value of previous elements
- Iterate through the array. When you find a value less than min value set it 
- if greater than min value, check if diff is greater than current max
'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        max_profit = 0
        curr_min = float("inf")

        for i in range(len(prices)):
            if prices[i] > curr_min:
                max_profit = max(prices[i] - curr_min, max_profit)
            elif prices[i] < curr_min:
                curr_min = prices[i]

        return max_profit
