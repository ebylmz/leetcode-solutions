from collections import deque

class Solution:
    def snakesAndLadders(self, board):
        
        """
        T(n) = O(n^2), In the worst case, we explore each square once.
        S(n) = O(n^2), visited and queue store up to n^2 positions
        """

        n = len(board)
        def get_row_col(pos):
            pos -= 1  # convert to 0-based
            row = n - 1 - (pos // n)
            col = (pos % n) if ((pos // n) % 2 == 0) else (n - 1 - (pos % n))
            return row, col

        visited = set()
        queue = deque([(1, 0)])  # (current square, steps)

        while queue:
            curr, steps = queue.popleft()
            if curr == n * n:
                return steps

            for move in range(1, 7):  # dice rolls 1–6
                next_pos = curr + move
                if next_pos > n * n:
                    continue
                r, c = get_row_col(next_pos)
                if board[r][c] != -1:
                    next_pos = board[r][c]

                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, steps + 1))

        return -1  # if end not reachable
