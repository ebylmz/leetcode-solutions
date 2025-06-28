class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        IDEA: A string is palindrome if it's reverse equivalent to itself. 
        Then we just need to find the common largest subsequence of s and reversed s.  

        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        def longestCommonSubseqLen(s1, s2):
            m, n = len(s1), len(s2)
            dp = [[0] * (n + 1) for _ in range(m + 1)]

            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    if s1[i] == s2[j]:
                        dp[i][j] = 1 + dp[i+1][j+1]
                    else:
                        dp[i][j] = max(dp[i+1][j], dp[i][j+1])
            return dp[0][0]

        return longestCommonSubseqLen(s, s[::-1])

        """
            b   a   c   a   \
        a   3   3   2   1   0
        c   2   2   2   1   0
        a   1   1   1   1   0
        b   1   0   0   0   0
        \   0   0   0   0   0
        """