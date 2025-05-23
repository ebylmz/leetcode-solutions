from collections import defaultdict

class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        
        """
            T(n) = O(n), S(n) = O(n)
            
            IDEA: Perform a BFS starting from node 0. Track which cities are reachable.
            Count how many edges must be reversed to ensure every node is reachable from node 0.
        """
        
        neighbours = defaultdict(list)
        connect = set()
        for u, v in connections:
            neighbours[u].append(v)
            neighbours[v].append(u)
            connect.add((u,v))

        num_changes = 0        
        reachable = [False] * n
        reachable[0] = True
        curr = [0]
        
        while curr:
            new_curr = []
            for c in curr:
                for n in neighbours[c]:
                    if not reachable[n]:
                        if (n, c) not in connect:
                            num_changes += 1
                        reachable[n] = True
                        new_curr.append(n)
            curr = new_curr
        return num_changes