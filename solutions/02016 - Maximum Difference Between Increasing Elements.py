class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        mn = 10**9
        best = -1
        for x in nums:
            if mn < x:
                best = max(best, x - mn)
            else:
                mn = min(mn, x)
        return best 