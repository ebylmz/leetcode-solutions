from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """

        """
        IDEA: Apply BFS
        Time Complexity: O(N*M), where N: number of rows, M: number of columns 
        Space Complexity: O(N*M), in the worst case (if all the cells are open) 
        """
        ROWS, COLS = len(maze), len(maze[0])
        q = deque()
        q.append((entrance[0], entrance[1], 0))
        maze[entrance[0]][entrance[1]] = '+'
        while q:
            r, c, step = q.popleft()
            # Check whether we've reached the exit
            # Otherwise continue to explore
            for i, j in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if i >= 0 and i < ROWS and j >= 0 and j < COLS and maze[i][j] == '.':
                    if i == 0 or i == ROWS - 1 or j == 0 or j == COLS - 1:
                        return step + 1
                    q.append((i, j , step + 1))
                    maze[i][j] = '+'
        return -1