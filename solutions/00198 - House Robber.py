class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        IDEA: Rob the current house only if doing so yields more money than skipping it and robbing the next house.
        
        Time Complexity = O(n) 
        Space Complexity = O(1) 
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        rob_next, rob_next_plus_one = nums[-1], 0
        for i in range(n - 2, -1, -1):
            current = max(nums[i] + rob_next_plus_one, rob_next)
            rob_next_plus_one = rob_next
            rob_next = current
        
        return rob_next
