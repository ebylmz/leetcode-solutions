from collections import defaultdict
from collections import deque

class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        IDEA:
        Build a graph of character equivalences using s1 and s2. Traverse connected 
        components with BFS to find groups of equivalent characters. For each group, 
        choose the lexicographically smallest character as the representative. 
        Use this mapping to transform baseStr into the smallest equivalent string.

        n: lenght of s1 and s2, m: length of baseStr, k: number of lowercase letters (26)
        Time Complexity: O(n + m), graph construction (O(n)), BFS traversal O(n + k)
        Space Complexity: O(n + m), edges
        """
        edges = defaultdict(set)
        for u, v in zip(s1, s2):
            edges[u].add(v)
            edges[v].add(u)

        def bfs(start):
            queue = deque([start])
            discovered = set([start])
            path = []
            
            while queue:
                node = queue.popleft()
                path.append(node)
                for neighbour in edges[node]:
                    if neighbour not in discovered:
                        discovered.add(neighbour)
                        queue.append(neighbour)
            return path

        char_to_rep  = {}
        for start in edges.keys():
            if start not in char_to_rep :
                equivalent = bfs(start)
                min_char = min(equivalent)
                for c in equivalent:
                    char_to_rep [c] = min_char

        result  = [c for c in baseStr]
        for i, c in enumerate(baseStr):
            if c in char_to_rep :
                result [i] = char_to_rep [c]
        
        return ''.join(result)