class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        """
        Time Complexity: O(m*n)
        Space Complexity: O(n)
        """

        total_count = 0
        m, n = len(mat), len(mat[0])
        heights = [0] * n  # histogram heights for each column

        for i in range(m):
            # Monotonic stack: (height, index, submatrix_count_up_to_here)
            stack = [(-1, -1, 0)] # dummy element to avoid empty stack issues
            for j in range(n):
                # Update histogram height
                heights[j] = heights[j] + 1 if mat[i][j] == 1 else 0

                # Find the first index which having smaller height than current height
                while heights[j] <= stack[-1][0]:
                    stack.pop()

                _, prev_j, prev_count = stack[-1]
                count = heights[j] * (j - prev_j) + prev_count # (curr_height * curr_width) + prev_count
                    
                stack.append((heights[j], j, count))
                total_count += count
        
        return total_count