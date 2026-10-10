class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        buy = prices[0]
        ans = 0

        for r in range(len(prices)):

            if prices[r] < buy:
                buy = prices[r]

            profit = prices[r] - buy

            
            ans = max(ans,profit)

        
        return ans









     