class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        
        return result