class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0 
        n = len(prices)
        buy = prices[0]
        sell =-1
        max = 0
        i = 0
        while i <= n-1:
            if(prices[i]<buy):
                buy = prices[i]
        
            max = prices[i] - buy if prices[i]-buy>max else max
            i+=1
        return max




