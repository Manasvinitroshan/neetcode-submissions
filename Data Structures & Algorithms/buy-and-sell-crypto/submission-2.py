class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = 0
        curr = 0
        answer = 0
        for right in range(buy+1,len(prices)):
            if prices[right] < prices[buy]:
                buy = right
                

            profit = prices[right] - prices[buy]
            answer = max(answer,profit)
            

        
        return answer




        