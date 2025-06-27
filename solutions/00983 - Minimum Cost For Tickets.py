class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        Time Complexity: O(3^n)
        Space Complexity: O(3^n)
        """
        dp = {}

        def dfs(i, last_date):
            if i == len(days):
                return 0
            if (i, last_date) in dp:
                return dp[(i, last_date)]    
            if days[i] <= last_date:
                dp[(i, last_date)] = dfs(i + 1, last_date)
            else:
                one_day = costs[0] + dfs(i + 1, days[i])
                seven_days = costs[1] + dfs(i + 1, days[i] + 6)
                thirty_days = costs[2] + dfs(i + 1, days[i] + 29)
                dp[(i, last_date)] = min(one_day, seven_days, thirty_days)
           
            return dp[(i, last_date)]

        return dfs(0, 0)