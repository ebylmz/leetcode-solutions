class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        T(n) = O(n)
        S(n) = O(1)
        """
        # XOR approach: a ^ a = 0, and a ^ 0 = a
        # So, XORing all numbers cancels out duplicates, leaving the single one.
        result = 0
        for num in nums:
            result ^= num
        return result