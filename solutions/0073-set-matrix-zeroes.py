class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Time Complexity: O(m * n)
        Space Complexity: O(1)
        """
        m, n = len(matrix), len(matrix[0])
        
        # Step 1: Check if first row and first column need zeroing
        first_row_zero = any(matrix[0][c] == 0 for c in range(n))
        first_col_zero = any(matrix[r][0] == 0 for r in range(m))
        
        # Step 2: Use first row & column as markers
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        # Step 3: Zero out cells based on markers
        for r in range(1, m):
            if matrix[r][0] == 0:
                for c in range(1, n):
                    matrix[r][c] = 0
                    
        for c in range(1, n):
            if matrix[0][c] == 0:
                for r in range(1, m):
                    matrix[r][c] = 0
        
        # Step 4: Zero out first row/column if needed
        if first_row_zero:
            for c in range(n):
                matrix[0][c] = 0
                
        if first_col_zero:
            for r in range(m):
                matrix[r][0] = 0