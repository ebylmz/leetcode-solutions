class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Keep the leftmost position from which the end is reachable
        goal = len(nums) - 1 

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0