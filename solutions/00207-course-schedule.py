class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """ 
        IDEA: 
            There should be any cycle in the directed graph formed by the prerequisites.
            We can use DFS to detect cycles in the graph.
            If we find a back edge during DFS, it indicates a cycle.
        Time Complexity: O(V + E), since each node is visited at most once
        Space Complexity: O(V)
        """
        adj_list = collections.defaultdict(list)
        for tar, src in prerequisites:
            adj_list[src].append(tar)
        
        visited = [False] * numCourses
        rec_stack = [False] * numCourses

        def is_cyclic(start):
            visited[start] = True
            rec_stack[start] = True

            for neighbor in adj_list[start]:
                if not visited[neighbor]:
                    if is_cyclic(neighbor): # Go deeper
                        return True
                elif rec_stack[neighbor]: # Found a back edge (cycle)
                    return True
            # Remove from rec_stack when done exploring
            rec_stack[start] = False
            return False

        # Check if there is a cycle in the graph
        for v in range(numCourses):
            if not visited[v]:
                if is_cyclic(v):
                    return False
        
        return True