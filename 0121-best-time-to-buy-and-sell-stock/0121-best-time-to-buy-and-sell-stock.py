class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #[7 1 5 3 6 4]
        buy = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if prices[i]<buy:
                buy = prices[i]
            
            if max_profit < prices[i]-buy:
                max_profit = prices[i]-buy
        return max_profit
            
