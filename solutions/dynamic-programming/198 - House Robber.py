class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # T(n) = O(n), S(n) = O(1)
        
        if len(nums) == 1:
            return nums[0]
        
        nums[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            nums[i] = max(nums[i - 1], nums[i - 2] + nums[i])
        
        return nums[-1]