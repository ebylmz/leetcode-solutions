class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        """
        T(n) = O(n), S(n) = O(n)

        i   binary  count[i]    offset    
        0   0000    0           0    
        1   0001    1           1
        2   0010    1           2
        3   0011    2           2
        4   0100    1           4
        5   0101    2           4
        6   0110    2           4
        7   0111    3           4
        8   1000    1           8
        9   1001    2           8
        """

        counts = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if i == offset * 2:
                offset *= 2
            counts[i] = counts[i - offset] + 1
        
        return counts