class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        top, bottom = m, -1
        left, right = n, -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i < top:
                        top = i
                    if i > bottom:
                        bottom = i
                    if j < left:
                        left = j
                    if j > right:
                        right = j
    
        if bottom == -1:  # means no '1' was found
            return 0

        return (bottom - top + 1) * (right - left + 1) 