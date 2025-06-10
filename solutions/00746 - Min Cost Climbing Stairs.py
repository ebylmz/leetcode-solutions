class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
            IDEA: Stair i can be reached from one or two previous stairs. Use DP.
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        
        a, b = cost[0], cost[1]
        for i in range(2, len(cost)):
            a, b = b, cost[i] + min(a, b)
        return min(a, b)