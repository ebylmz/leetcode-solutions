class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        if numRows == 1 or numRows == len(s):
            return s
        
        rows = [''] * numRows
        i = 0
        going_down = False
        for c in s:
            rows[i] += c
            # Change direction if we are at the top or bottom row
            if i == 0 or i == numRows - 1:
                going_down = not going_down
            i += 1 if going_down else -1
        
        return ''.join(rows)