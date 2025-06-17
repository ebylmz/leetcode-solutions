class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        """
        IDEA: Keep track of the differences in each index.
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
        dp = [{} for _ in range(len(nums))]
        mx = 2
        for i in range(1, len(nums)):
            for j in range(i):
                difference = nums[i] - nums[j]
                dp[i][difference] = dp[j].get(difference, 1) + 1
                mx = max(mx, dp[i][difference])
        return mx