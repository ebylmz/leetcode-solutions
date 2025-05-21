class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        
        # T(n) = O(n) (because we look at every cell in the adjacency matrix once across all DFS traversals)
        # S(n) = O(n) (in the worst case (completely connected graph), DFS may go n levels deep)

        n = len(isConnected)
        visited = [False] * n

        def dfs(city):
            visited[city] = True
            for neighbour in range(n):
                if not visited[neighbour] and isConnected[city][neighbour] == 1:
                    dfs(neighbour)

        provinces = 0
        for city in range(n):
            if not visited[city]:
                provinces += 1
                dfs(city)
        
        return provinces
