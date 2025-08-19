class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """
        Idea: Every new zero extends all previous zero-subarrays and also forms a new single-element subarray.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        count, streak = 0, 0
        for i in range(len(nums)):
            streak = streak + 1 if nums[i] == 0 else 0
            count += streak

        return count