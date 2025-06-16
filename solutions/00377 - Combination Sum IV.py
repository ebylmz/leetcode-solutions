class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        n: target, m: len(nums)
        Time Complexity: O(n * m), since we need to try each possibility once 
        Space Complexity: O(n)
        """

        dp = [0] * (target + 1)
        dp[0] = 1 # Only way to get sum 0 is by picking nothing — 1 way
        
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]        
        return dp[target]