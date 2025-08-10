class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        """
        Time Complexity: O(1), bounded by number of digits (at most 9) and 32 powers of 2
        Space Complexity: O(1), since we store a fixed-size set
        """
        def digit_signature(x):
            return ''.join(sorted(str(x)))

        powers = set()
        current = 1
        for _ in range(32):
            powers.add(digit_signature(current))
            current <<= 1
        
        return digit_signature(n) in powers