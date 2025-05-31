class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        """
        IDEA: 
        Create a DP table where distances[i][j] represents the minimum number of operations.
        For the cell distances[i][j], we know the number of convertion needed for
        distances[i-1][j-1], distances[i][j-1] and distances[i-1][j] 

        T(n) = O(n*m) 
        S(n) = O(n*m)

          / h o r s e
        / 0 1 2 3 4 5
        h 1 0 1 2 3 4
        o 2 1 0 1 2 3
        r 3 2 1 0 1 2
        """

        rows, cols = len(word1) + 1, len(word2) + 1
        distances = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            distances[r][0] = r  
        for c in range(cols):
            distances[0][c] = c

        for r in range(1, rows):
            for c in range(1, cols):
                if word1[r-1] == word2[c-1]:
                    distances[r][c] = distances[r-1][c-1] 
                else:
                    distances[r][c] = min(
                        distances[r][c-1],  # Insert
                        distances[r-1][c],  # Delete   
                        distances[r-1][c-1] # Replace
                    ) + 1

        return distances[rows-1][cols-1]
