class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        buy = prices[0]

        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]

            
            profit = prices[i] - buy

            res = max(res,profit)

        return res
        