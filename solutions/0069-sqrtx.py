class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Time Complexity: O(logn)
        Space Complexity: O(1)
        """
        l, r = 0, x
        while l <= r:
            m = (l + r) // 2
            guess = m * m
            if guess > x:
                r = m - 1 
            elif guess < x:
                l = m + 1
            else:
                return m  

        return r