class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # T(n) = O(n), S(n) = O(n)
        seen = {}
        for i, n in enumerate(nums):
            pair = target - n
            if pair in seen:
                return [seen[pair], i]
            seen[n] = i