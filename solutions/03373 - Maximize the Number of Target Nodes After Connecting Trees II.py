class Solution(object):
    def maxTargetNodes(self, edges1, edges2):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :rtype: List[int]
        """
        
        """
        Idea: Set each node T or F, no two node having edge can has the same value
        n: number of nodes in tree1, m: number of nodes in tree2
        T(n) = O(n + m), since all the edges need to be traversed in both trees
        S(n) = O(n + m), due to marks set
        """

        def create_adj_list(edges):
            adj = collections.defaultdict(list)
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj
        
        def bfs(start, edges, n):
            adj = create_adj_list(edges)

            marks = [None] * n
            q = collections.deque()
            q.append(start)

            mark = False # Mark the start node as False
            while q:
                n = len(q)
                # Process n nodes on the current level
                for _ in range(n): 
                    curr = q.popleft()
                    marks[curr] = mark
                    for neighbor in adj[curr]:
                        if marks[neighbor] is None:
                            q.append(neighbor)
                # Reverse the color code for the next level 
                mark = not mark
            return marks

        n, m = len(edges1) + 1, len(edges2) + 1
        marks1 = bfs(0, edges1, n)
        marks2 = bfs(0, edges2, m)

        def count_marks(marks):
            t = sum(marks)
            f = len(marks) - t
            return t, f

        t1, f1 = count_marks(marks1)
        t2, f2 = count_marks(marks2)

        result = [max(t2, f2)] * n
        for i in range(n):
            result[i] += t1 if marks1[i] else f1

        return result