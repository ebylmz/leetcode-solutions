class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        """
        :type edges: List[int]
        :type node1: int
        :type node2: int
        :rtype: int
        """

        """
        IDEA: Measure the distances from starting node to all the other nodes
        T(n) = O(n), since we visit each edges at most twice
        S(n) = O(n), due to distances array
        """

        def measure_distances(start, edges):
            distances = [float("inf")] * len(edges)
            curr = start
            n = 0
            while curr != -1 and distances[curr] == float("inf"):
                distances[curr] = n
                n += 1
                curr = edges[curr]
            return distances

        distances1 = measure_distances(node1, edges)
        distances2 = measure_distances(node2, edges)

        min_dist, min_i = float("inf"), -1
        for i, (a, b) in enumerate(zip(distances1, distances2)):
            curr_dist = max(a, b)
            if curr_dist < min_dist:
                min_dist = curr_dist
                min_i = i
        return min_i 