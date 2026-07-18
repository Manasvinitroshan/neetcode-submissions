class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        buy = prices[0]

        for r in range(len(prices)):
            if prices[r] < buy:
                buy = prices[r]

            
            profit = prices[r] - buy

            max_profit = max(max_profit,profit)

        
        return max_profit
        