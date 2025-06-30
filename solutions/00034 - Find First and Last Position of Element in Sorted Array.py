class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(nums, target):
            """
            finds the first index ≥ target
            """
            l, r = 0, len(nums)
            while l < r:
                m = (l + r) // 2
                if target > nums[m]:
                    l = m + 1
                else:
                    r = m
            return l

        def upper_bound(nums, target):
            """
            finds the first index > target
            """

            l, r = 0, len(nums)
            while l < r:
                m = (l + r) // 2
                if target >= nums[m]:
                    l = m + 1
                else:
                    r = m
            return l

        begin = lower_bound(nums, target)
        if begin == len(nums) or nums[begin] != target:
            return [-1, -1]

        end = upper_bound(nums, target) - 1
        return [begin, end]