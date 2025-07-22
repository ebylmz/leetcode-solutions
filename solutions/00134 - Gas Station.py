class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """"
        n = len(gas)
        start = curr = 0
        tank = 0
        visits = 0

        while visits < n:
            tank += gas[curr] - cost[curr] 
            visits += 1
            while tank < 0 and visits < n:
                start = n - 1 if start == 0 else start - 1
                tank += gas[start] - cost[start]
                visits += 1
            curr += 1

        return -1 if tank < 0 else start