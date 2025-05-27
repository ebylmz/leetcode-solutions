from collections import defaultdict

class Solution(object):
    def largestPathValue(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """

        """
        n: number of nodes, m: number of edges
        T(n, m) = O(n + m), since every node and edge visited only once  
        S(n, m) = O(n + 26*n) = O(n), dp counts and max recursion depth  
        """

        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
        
        def dfs(node):
            if node in path:
                # Cycle detected: current node is already in the current DFS path
                return float("inf")
            if node in visited:
                # Already processed this node and max value was recorded
                return 0  

            color_index = ord(colors[node]) - ord('a')
            counts[node][color_index] = 1
            visited.add(node)
            path.add(node)
            for nei in adj[node]:
                v = dfs(nei)
                if dfs(nei) == float("inf"): 
                    return v # Termination
                # Update the color counts
                for c in range(26):
                    counts[node][c] = max(
                        counts[node][c], 
                        (1 if color_index == c else 0) + counts[nei][c]
                    )

            path.remove(node)
            return max(counts[node])

        n = len(colors)
        maxv = 0
        visited, path = set(), set()

        # counts[i][c] represents the max number of color `c` seen in any path starting at node `i`
        counts = [[0] * 26 for _ in range(n)] 
        for i in range(n):
            maxv = max(dfs(i), maxv)
            if maxv == float("inf"):
                return -1  # Cycle detected
        
        return maxv