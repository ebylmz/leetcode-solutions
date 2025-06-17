class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        """
        IDEA: Did I already build a subsequence ending at num - difference
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        dp = {}
        max_len = 0

        for num in arr:
            dp[num] = dp.get(num - difference, 0) + 1
            max_len = max(max_len, dp[num])

        return max_len
