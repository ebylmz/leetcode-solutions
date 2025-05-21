class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # T(n) = O(n), S(n) = O(1)        

        if n == 1 or n == 2:
            return n

        # Number of combinations in previous steps
        prev1, prev2 = 1, 2 
        for i in range(2, n):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr
        return prev2