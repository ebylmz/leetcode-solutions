class Solution(object):
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        """
        
        """
        3x7 grid 
        [1, 1, 1, 1, 1, 1, 1]
        [1, 2, 3, 4, 5, 6, 7]
        [1, 3, 6,10,15,21,28]
        """

        grid = [[1 for _ in range(n)]] * m
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[m-1][n-1]