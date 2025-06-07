class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = [[None] * len(s2) for _ in range(len(s1))]

        def bfs(i, j):
            if i == len(s1):
                return sum(ord(c) for c in s2[j:])
            if j == len(s2):
                return sum(ord(c) for c in s1[i:])
            
            if dp[i][j] is not None:
                return dp[i][j]

            if s1[i] == s2[j]:
                dp[i][j] = bfs(i + 1, j + 1)
            else:
                c1 = ord(s1[i]) + bfs(i + 1, j)
                c2 = ord(s2[j]) + bfs(i, j + 1)
                dp[i][j] = min(c1, c2)

            return dp[i][j]

        return bfs(0, 0)
