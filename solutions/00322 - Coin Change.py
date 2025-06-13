class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        IDEA: DP Bottom-up
        Time Complexity: O(amount * len(coins))
        Space Complexity: O(amount)
        """
        dp = [float("inf") for i in range(amount + 1)]
        dp[0] = 0
        coins.sort()

        for a in range(1, amount + 1):
            for coin in coins:
                if coin > a:
                    break
                dp[a] = min(dp[a], 1 + dp[a - coin])
        
        return dp[amount] if dp[amount] != float("inf") else -1 