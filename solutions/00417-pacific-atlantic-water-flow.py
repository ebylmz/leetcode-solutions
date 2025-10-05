class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        """
        m, n = len(heights), len(heights[0])
        
        def bfs(starts):
            visited = set(starts)
            queue = collections.deque(starts)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while queue:
                i, j = queue.popleft()
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if (0 <= ni < m and 0 <= nj < n 
                        and (ni, nj) not in visited
                        and heights[ni][nj] >= heights[i][j]):
                        visited.add((ni, nj))
                        queue.append((ni, nj))
            return visited

        pacific_starts = [(i, 0) for i in range(m)] + [(0, j) for j in range(n)]
        atlantic_starts = [(i, n - 1) for i in range(m)] + [(m - 1, j) for j in range(n)]

        pacific_flow = bfs(pacific_starts)
        atlantic_flow = bfs(atlantic_starts)
        
        return list(pacific_flow & atlantic_flow)