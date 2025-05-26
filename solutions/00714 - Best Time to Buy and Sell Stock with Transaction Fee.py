class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        """
        T(n) = O(2n), every index we calculate the result twice for two state (buy-sell, do nothing) 
        S(n) = O(3n), 2n space for the dp array and n space for the recursion stack
        """
        
        n = len(prices)
        dp = [[None for j in range(2)] for i in range(n)]

        def explore(i, can_buy):
            if i == n:
                return 0
            elif dp[i][can_buy]:
                return dp[i][can_buy]
            
            if can_buy == 1:
                # Case 1: Buy          
                buy_sell = -prices[i] + explore(i + 1, 0)
            else:
                # Case 2: Sell        
                buy_sell = prices[i] - fee + explore(i + 1, 1)
            # Case 3: Do nothing                
            move_on = explore(i + 1, can_buy)

            dp[i][can_buy] = max(buy_sell, move_on)
            return dp[i][can_buy]

        return explore(0, True)