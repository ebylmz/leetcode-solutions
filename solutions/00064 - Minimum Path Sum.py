class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        """
        IDEA: A cell can only be reached from its top or left cells
        Time Complexity: O(n*m), where n: number of rows, m: number of columns
        Space Complexity: O(1)
        """
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(1, ROWS):
            grid[r][0] += grid[r-1][0] 
        for c in range(1, COLS):
            grid[0][c] += grid[0][c-1] 

        for r in range(1, ROWS):
            for c in range(1, COLS):
                grid[r][c] += min(grid[r-1][c], grid[r][c-1])
        return grid[-1][-1]
