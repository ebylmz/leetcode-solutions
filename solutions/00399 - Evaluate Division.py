class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        """
        n: number of nodes, m: number of edges, q: number of queries
        T(n) = O(m + n*q), creation of edges takes O(m), and DFS may visit up to all n nodes O(q*n)  
        S(n) = O(m + n + q), due to edges adj list, results array, and recursion stack
        """

        """
        queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
        equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0]
          3/2    5/2            5
        a ---> b ---> c     bc ---> cd
          <---   <---          <---
          2/3    2/5            1/5
        """

        # Convert the equations into directed graph with weights on edges
        edges = collections.defaultdict(dict)
        for (a, b), v in zip(equations, values):
            edges[a][b] = v
            edges[b][a] = 1 / v
        
        def find_dfs(start, end, visited):
            visited.add(start)
            if start == end:
                return 1.0
            # Continue searching from the neighbours
            for neighbour in edges[start].keys():
                if neighbour not in visited:
                    v = find_dfs(neighbour, end, visited)
                    if v > 0:
                        # We find the correct path leading to target
                        return edges[start][neighbour] * v
            return -1.0
        results = [0] * len(queries)
        for i, (a, b) in enumerate(queries):
            if a in edges and b in edges:
                results[i] = find_dfs(a, b, set())
            else:
                results[i] = -1.0
        
        return results
