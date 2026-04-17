class Solution(object):
    def maxProfit(self,prices):
        n = len(prices)
        if n == 0: return 0
    
    # Create our memory: dp[day][state]
    # State 0: Empty-handed, State 1: Holding
        dp = [[0] * 2 for _ in range(n)]
    
    # Base Case: Day 0
        dp[0][0] = 0
        dp[0][1] = -prices[0]
    
        for i in range(1, n):
        # State 0: Either I stayed empty, or I sold today
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        
        # State 1: Either I stayed holding, or I bought today (only once!)
        # Since we only buy once, buying today means profit is just -price
            dp[i][1] = max(dp[i-1][1], -prices[i])
        
        return dp[n-1][0]