class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        Time Complexity: O(m*n)
        Space Complexity: O(n)
        """
        m, n = len(matrix), len(matrix[0])
        prev = [0] * (n + 1)  # extra padding to avoid bounds checking
        curr = [0] * (n + 1)
        max_len = 0

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    curr[j] = 1 + min(curr[j + 1], prev[j + 1], prev[j])
                    max_len = max(max_len, curr[j])
                else:
                    curr[j] = 0
            prev, curr = curr, prev    # swap for next iteration
        return max_len * max_len