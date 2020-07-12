"""
Leetcode:322. Coin Change

Attempts: 1
Completed: Y
Acheived Ideal: N -> can skip evaluating when you know that you cant best the current min coin count

Time Complexity: O(n * amount)
Space Complexity: O(amount)

Pattern: Dynamic Programming
Technique: Bottom up 

Problems Encountered: Need to catch case when the min value in float("inf")
Other Solutions: See Below

"""


# Works but not very fast
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        minCoinsDict = {0: 0}

        for coin in coins:
            minCoinsDict[coin] = 1

        for i in range(1, amount + 1):
            minNum = float("inf")
            for coin in coins:
                coinDiff = i - coin
                if coinDiff >= 0 and minCoinsDict[coinDiff] != -1:
                    minNum = min(minNum, minCoinsDict[coinDiff] + 1)
            if minNum == float("inf"):
                minCoinsDict[i] = -1
            else:
                minCoinsDict[i] = minNum
        return minCoinsDict[amount]


"""
Solution is in python 3 but incredibly intelligent. 
First sort the coins from biggest to smallest because you want to evaluate the bigger coins first
Then looking through the coins from big to small, check if you can even accomplish the remaining amount with the largest coins
that you have given the remaining number of coins you can use to beat the current min number of coins -> dont bother 
evaluating if you cant
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        min_coins = float("inf")

        def count_coins(start_coin, coin_count, remaining_amount):
            nonlocal min_coins

            if remaining_amount == 0:
                min_coins = min(min_coins, coin_count)
                return

            # Iterate from largest coins to smallest coins
            for i in range(start_coin, len(coins)):
                remaining_coin_allowance = min_coins - coin_count
                max_amount_possible = coins[i] * remaining_coin_allowance

                if (
                    coins[i] <= remaining_amount
                    and remaining_amount < max_amount_possible
                ):
                    count_coins(i, coin_count + 1, remaining_amount - coins[i])

        count_coins(0, 0, amount)
        return min_coins if min_coins < float("inf") else -1

