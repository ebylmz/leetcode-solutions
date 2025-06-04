from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        """
        IDEA: Apply BFS
        Worst Case Time Complexity: O(n*m), where n: number of rows, m: number of columns
        Space Complexity: O(1) 
        """

        ROWS, COLS = len(grid), len(grid[0])
        rotten = deque()
        fresh = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1: # Fresh orange
                    fresh += 1
                elif grid[i][j] == 2: # Rotten orange
                    rotten.append((i,j))

        minutes = 0
        while rotten and fresh > 0:
            n = len(rotten)
            minutes += 1
            for _ in range(n):
                r, c = rotten.popleft()

                for i, j in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
                    if i >= 0 and j >= 0 and i < ROWS and j < COLS and grid[i][j] == 1:
                        grid[i][j] = 2 # Make it rotten
                        rotten.append((i,j))
                        fresh -= 1
                        if fresh == 0:
                            return minutes
        
        return minutes if fresh == 0 else -1