class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Time Complexity: O(n! * n), n! permutation and each of them takes O(n) time for copying at the end
        Space Complexity: O(n! * n)
        """
        res = []

        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        
        backtrack(0)
        return res