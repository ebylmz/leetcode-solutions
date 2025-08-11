class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Idea: XOR of any number with itself is 0, and XOR or any number with zero equals to itself.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        ans = 0
        for num in nums:
            ans ^= num
        return ans