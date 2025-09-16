class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        Idea: 
            Model the equations as a graph where each variable is a node and each equation is a directed edge with a weight equal to the division value. 
            To answer each query, perform BFS to find the path from the numerator to the denominator and multiply the weights along the path.
        
        Q: number of queries, E: number of edges, V: the number of distict variables
        Time Complexity: O(Q * E), since each BFS can, in the worst case, explore all edges
        Space Complexity: O(E + V), adjancency list and variables set
        """

        # Create an undirected graph represented by an adjacency list
        variables = set()
        edges = collections.defaultdict(list)
        for (a, b), v in zip(equations, values):
            edges[a].append((b, v))
            edges[b].append((a, 1.0 / v))
            variables.add(a)
            variables.add(b)

        def bfs(start: str, target: str) -> float:
            if start not in variables or target not in variables:
                return -1.0
            
            visited = set([start])
            queue = collections.deque([(start, 1.0)])
            
            while queue:
                node, val = queue.popleft()
                if node == target:
                    return val

                for neighbour, w in edges[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append((neighbour, val * w))

            return -1.0
        
        return [bfs(a, b) for a, b in queries]