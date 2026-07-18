class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        for i in range(len(prices)):
            start = prices[i]
            for j in range(i+1,len(prices)):
                profit = prices[j] - start

                maximum = max(maximum,profit)

        return maximum



        