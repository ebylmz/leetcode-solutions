class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        m: len(s), n = len(t)
        Time Complexity: O(m*n)
        Space Complexity: O(m)
        """
        m, n = len(s), len(t)

        # dp[i][j] will store the number of distinct subsequences of s[i:] matching t[j:]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base case: An empty target can always be matched by deleting all remaining characters in s
        for i in range(m + 1):
            dp[i][n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = dp[i + 1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]

        return dp[0][0]
