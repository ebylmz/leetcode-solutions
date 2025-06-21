class Solution:
    def minInsertions(self, s: str) -> int:
        """
        IDEA: Find the longest palindromic subsequence. The characters not in it need to be inserted.
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        def longestCommonSubsequence(s1, s2):
            m, n = len(s1), len(s2)
            dp = [0] * (n + 1)
            for i in range(m - 1, -1, -1):
                prev_dp = dp[:]
                for j in range(n - 1, -1, -1):
                    if s1[i] == s2[j]:
                        dp[j] = 1 + prev_dp[j + 1]
                    else: 
                        dp[j] = max(prev_dp[j], dp[j + 1])
            
            return dp[0]

        return len(s) - longestCommonSubsequence(s, s[::-1])