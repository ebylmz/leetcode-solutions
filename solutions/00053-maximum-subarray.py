class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        IDEA: At each index i, the maximum subarray ending at i either:
            - extends the maximum subarray ends at i-1, or
            - start fresh from i
        """
        best, max_ending = nums[0], nums[0]
        for i in range(1, len(nums)):
            max_ending = max(max_ending + nums[i], nums[i])
            best = max(best, max_ending)    
        
        return best