class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        N = len(nums)
        dp = [1] * N 

        for i in range(N - 2, -1, -1):
            for j in range(i+1, N):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)