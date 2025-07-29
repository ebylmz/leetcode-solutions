class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        """
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        """
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        """
        Track the previous cell to avoid trivial backward steps.
        If you encounter a visited cell that's not the previous one, and it's the same character, a cycle is found.
        """
        def dfs(i, j, from_i, from_j, char):
            if visited[i][j]:
                return True

            visited[i][j] = True
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == char:
                    if (ni, nj) == (from_i, from_j): # Don't go back
                        continue
                    if dfs(ni, nj, i, j, char):
                        return True
            return False

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True

        return False 