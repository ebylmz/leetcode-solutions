class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # T(n) = O(n), S(n) = O(n^2), where n = numRows
        rows = []
        for i in range(0, numRows):
            row = [1] * (i + 1)
            # Padding with 1
            for j in range(1, i):
                row[j] = rows[i-1][j-1] + rows[i-1][j]
            rows.append(row)        
        return rows