from collections import defaultdict
from collections import deque

class Solution(object):
    def maxTargetNodes(self, edges1, edges2, k):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        
        """
        T(n) = O(n^2 + m^2), since each node visited n times for tree 1, and m times for tree 2
        S(n) = O(n + m), due to visited set
        """

        def create_adj_list(edges):
            adj = defaultdict(list)
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj

        def bfs_count(start, adj, k):
            if k < 0:
                return 0
            
            visited = set()
            q = deque()
            q.append(start)
            count = 0
            while q and k >= 0:
                n = len(q)
                # Process the current layer
                for _ in range(n):
                    curr = q.popleft()
                    visited.add(curr)
                    count += 1
                    for nei in adj[curr]:
                        if nei not in visited:
                            q.append(nei)
                # Decrease the distance
                k -= 1
            
            return count

        adj1, adj2 = create_adj_list(edges1), create_adj_list(edges2)
        n, m = len(edges1) + 1, len(edges2) + 1
        counts = [0] * n
        maxv = 0
        # Apply BFS for the second tree with path lenght of k - 1
        for i in range(m):
            maxv = max(maxv, bfs_count(i, adj2, k - 1))
                
        # Apply BFS for the first tree with path lenght of k
        for i in range(n):
            counts[i] = bfs_count(i, adj1, k) + maxv
        
        return counts