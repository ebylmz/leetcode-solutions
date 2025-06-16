class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        Time Complexity: O(l * m * n), where l: len(strs) (since each subproblem is computed only once).
        Space Complexity: O(l * m * n)
        """

        dp = {}
        counts = [(s.count('0'), s.count('1')) for s in strs]        

        def dfs(i, m, n):
            if i == len(strs):
                return 0

            if (i, m, n) in dp:
                return dp[(i, m, n)]
            
            zeros, ones = counts[i]

            # Option 1: Skip current string
            res = dfs(i + 1, m, n)

            # Option 2: Include current string if it fits
            if m >= zeros and n >= ones:
                res = max(res, 1 + dfs(i + 1, m - zeros, n - ones))

            dp[(i, m, n)] = res
            return res

        return dfs(0, m, n)