class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0 
        n = len(prices)
        buy = float('inf')
        sell =-1
        max = 0
        i = 0
        while i <= n-1:
            if(prices[i]<buy):
                buy = prices[i]
            sell = prices[i]
            max = sell - buy if sell-buy>max else max
            i+=1
        return max




