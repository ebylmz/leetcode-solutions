class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Time Complexity: O((amount + 1) * (len(coins) + 1))
        Space Complexity: O((amount + 1) * (len(coins) + 1))
        """
        num_coins = len(coins)
        dp = [[0] * (num_coins + 1) for _ in range(amount + 1)]
        
        for i in range(num_coins + 1):
            dp[0][i] = 1
        
        for a in range(1, amount + 1):
            for i in range(num_coins - 1, -1, -1):
                dp[a][i] = dp[a][i + 1]
                c = coins[i]
                if a - c >= 0:
                    dp[a][i] += dp[a - c][i]
        
        return dp[amount][0]