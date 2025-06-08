class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Time Complexity: O(n*m)
        Space Complexity: O(n*m) 
        """

        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]

    """
        a   c   e   \
    a   3   2   1   0
    b   2   2   1   0
    c   2   2   1   0
    d   1   1   1   0
    e   1   1   1   0
    \   0   0   0   0
    """