class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        """
        3x7 grid 
        [1, 1, 1, 1, 1, 1, 1]
        [1, 2, 3, 4, 5, 6, 7]
        [1, 3, 6,10,15,21,28]
        """
        
        # T(n, m) = O(n*m), S(n, m) = O(n*m)

        grid = [[1 for i in range(n)]] * m
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[m-1][n-1]