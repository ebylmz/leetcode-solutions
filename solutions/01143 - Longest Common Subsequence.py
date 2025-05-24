class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        """
             a,c,e
          [0,0,0,0]
        a [0,1,1,1]
        c [0,1,2,2]
        """

        # T(n,m) = O(n*m), S(n,m) = O(n*m) 

        rows, cols = len(text1) + 1, len(text2) + 1
        dp = [[0 for j in range(cols)] for i in range(rows)]

        for i in range(1, rows):
            for j in range(1, cols):
                if text2[j-1] != text1[i-1]:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                else:   
                    dp[i][j] = dp[i-1][j-1] + 1
                    if dp[i][j] == i:
                        # We reached the maximum subsequence length
                        for k in range(j+1, cols):
                            dp[i][k] = dp[i][j]
        return dp[rows-1][cols-1]