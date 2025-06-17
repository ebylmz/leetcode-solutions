class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        """
        Time Complexity: O(high)
        Space Complexity: O(high)
        """

        MOD = 10**9 + 7

        dp = [0] * (high + 1)
        dp[0] = 1 # There is exactly one empty string

        for i in range(1, high + 1):
            if i - zero >= 0:
                dp[i] = (dp[i] + dp[i - zero]) % MOD
            if i - one >= 0:
                dp[i] = (dp[i] + dp[i - one]) % MOD

        return sum(dp[low:high+1]) % MOD            