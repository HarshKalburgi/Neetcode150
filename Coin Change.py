# Coin Change
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.
# code
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + ([float('inf')] * amount)
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[-1] == float('inf'):
            return -1
        return dp[-1]
