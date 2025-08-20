class Solution:
    def findMin(self, nums: List[int]) -> int:
        """   
        Time Complexity: O(logn)
        Space Complexity: O(1)
        """
        l, r = 0, len(nums) - 1
        while l < r and nums[l] > nums[r]:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
            
        return nums[l]