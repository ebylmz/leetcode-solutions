class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        pairs.sort(key=lambda x: x[0])
        n = len(pairs)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)