class Solution:
    def numSquares(self, n: int) -> int:
        """
        Time Complexity: O(n * sqrt(n))
        Space Complexity: O(n)
        """

        dp = [i for i in range(n + 1)]
        for target in range(1, n + 1):
            for s in range(1, int(sqrt(target)) + 1):
                dp[target] = min(dp[target], 1 + dp[target - s**2])
        return dp[n]